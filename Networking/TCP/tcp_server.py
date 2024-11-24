import socket
import threading 

ip = input("What IP would you like to use for your TCP server? Try 0.0.0.0 it is useful to listen everywhere: \n")
port = int(input("What port would you like to use for your TCP server?: \n"))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket object
    server.bind((ip, port)) # Binds the socket to the selected ip and port
    server.listen(5) # Set the server to listen with a max of 5 connections
    print(f"[*] Listening on {ip}:{port}") # Prints out "[*] Listening on ip:port"

    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(4096)
        print(f"[*] Received: {request.decode('utf-8')}")
        sock.send(b"ACK")

if __name__ == '__main__':
    main()
