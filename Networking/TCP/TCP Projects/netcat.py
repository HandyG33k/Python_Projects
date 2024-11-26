# Import reqired libraies 
import socket 
import argparse
import shlex
import subprocess
import sys
import textwrap
import threading

# Create a function called execute that takes a command and strips the leading and trailing whitespace if not a command ends the function then uses check_output to run the command using shlex.split to convert the command into arguments, then redirects to STDOUT and decodes the bytes to a string effectivlly running the command.
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr=subprocess.STDOUT)
    return output.decode()

# Creating the NetCat object
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

# Function to connect to target IP and port
    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
          self.socket.send(self.buffer)

        try:
            while True:
              recv_len = 1
              response = ''
              while recv_len:
                  data = self.socket.recv(4096)
                  recv_len = len(data)
                  response += data.decode()
                  if recv_len < 4096:
                      break
              if response:
                   print(response)
                   buffer = input('> ')
                   buffer += '\n'
                   self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('User Terminated')
            self.socket.close()
            sys.exit()

# Function to listen
    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
          )
            client_thread.start()

# Function to handle the command line arguments
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

            with open(self.args.upload, 'wb') as f:
                 f.write(file_buffer)
            message = f"Saved file {self.args.upload}\n "
            client_socket.send(message.encode())

        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while '\n' not in cmd_buffer.decode():
                         cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                         client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'server killed {e}')
                    self.socket.close()
                    sys.exit()


# Setup the command line interface 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            netcat.py -t 192.168.1.2 -p 1337 -l -c # Command Shell
            netcat.py -t 192.168.1.2 -p 1337 -l -u=test.txt # Upload a File
            netcat.py -t 192.168.1.2 -p 1337 -l -e \" cat /etc/passwd\" # Execute a Command
            netcat.py -t 192.168.1.2 -p 1337 # Connect to a server
            echo 'Test' | ./netcat.py -t 192.168.1.2 -p 1337 # Echo text to server port 1337
            '''))
    parser.add_argument('-t', '--target', default='192.168.1.1', help='Set IP Address Default 192.168.1.1')
    parser.add_argument('-p', '--port', type=int, default='1337', help='Set target port Default 1337')
    parser.add_argument('-l', '--listen', action='store_true', help='Set to listen')
    parser.add_argument('-c', '--command', action='store_true', help='Command shell')
    parser.add_argument('-u', '--upload', help='Upload file')
    parser.add_argument('-e', '--execute', help='Execute a command')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()


    
    
