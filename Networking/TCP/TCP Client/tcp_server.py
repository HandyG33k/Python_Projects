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
        client, address = server.accept()  # Blocks till a connection is received Client = a new socket for the connected client to send and receive to. address = a tuple that uses the client that connects to assign an ip to address[0] and a port to address[1] 
        print(f"[*] Accepted connection from {address[0]}:{address[1]}") # Prints [*] Accepted Connection from then uses the address[0] and address[1] assignments to print the ip:port combo 
        client_handler = threading.Thread(target=handle_client, args=(client,)) # creates a variable client_handler that creates a thread the server can use to talk to the client with targets the function handle_client and passes the argument client socket to handle_client
        client_handler.start() # Starts the thread created

def handle_client(client_socket): # Creates the handle_client function with client_socket as its argument  to be used in the main function 
    with client_socket as sock:  # Will handle closing the socket when the function ends
        request = sock.recv(4096) # Will receive up to 4096 bytes of data 
        print(f"[*] Received: {request.decode('utf-8')}") # Prints out the data received in utf-8 encoding 
        sock.send(b"ACK\n") # Sends the client ACK as an acknolegment of data received 

if __name__ == '__main__':
    main()
