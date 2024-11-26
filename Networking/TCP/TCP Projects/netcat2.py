import socket
import argparse
import shlex
import subprocess
import sys
import textwrap
import threading


def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    try:
        output = subprocess.check_output(shlex.split(cmd),
                                         stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output.decode()}"


class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            while True:
                response = ''
                while True:
                    data = self.socket.recv(4096)
                    if not data:
                        break
                    response += data.decode()
                if response:
                    print(response)
                    buffer = input('> ') + '\n'
                    self.socket.send(buffer.encode())
        except (KeyboardInterrupt, ConnectionResetError):
            print('Connection closed.')
            self.socket.close()
            sys.exit()

    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
            )
            client_thread.start()

    def handle(self, client_socket):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())

        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break

            # Safe file handling
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f"Saved file {self.args.upload}\n"
            client_socket.send(message.encode())

        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while b'\n' not in cmd_buffer:
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except (UnicodeDecodeError, Exception) as e:
                    client_socket.send(f"Error: {str(e)}\n".encode())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            netcat.py -t 192.168.1.2 -p 1337 -l -c # Command Shell
            netcat.py -t 192.168.1.2 -p 1337 -l -u=test.txt # Upload a File
            netcat.py -t 192.168.1.2 -p 1337 -l -e "cat /etc/passwd" # Execute a Command
            netcat.py -t 192.168.1.2 -p 1337 # Connect to a server
            echo 'Test' | ./netcat.py -t 192.168.1.2 -p 1337 # Echo text to server port 1337
        ''')
    )
    parser.add_argument('-t', '--target', default='192.168.1.1', help='Set IP Address Default 192.168.1.1')
    parser.add_argument('-p', '--port', type=int, default=1337, help='Set target port Default 1337')
    parser.add_argument('-l', '--listen', action='store_true', help='Set to listen')
    parser.add_argument('-c', '--command', action='store_true', help='Command shell')
    parser.add_argument('-u', '--upload', help='Upload file')
    parser.add_argument('-e', '--execute', help='Execute a command')
    args = parser.parse_args()

    buffer = sys.stdin.read() if not args.listen and not sys.stdin.isatty() else ''

    nc = NetCat(args, buffer.encode())
    nc.run()
