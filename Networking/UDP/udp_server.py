import socket

# Create a UDP server socket 
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# User input for Server IP address
server_ip = input("What IP Addres would you like to bind the UDP server to?: ")
# server_ip_int = int(server_ip)

# User input for UDP port
server_port = input("What port would you like the server to listen on?: ")
server_port_int = int(server_port)

# Bind the UDP server to the requested ip and port
server.bind((server_ip, server_port_int))

print(f'Server is listening on {server_ip} and {server_port_int}')
while True:
    data , addr = server.recvfrom(4096)
    print(f"Received: {data.decode()} from {addr}")
    server.sendto(data, addr)

server.close()
