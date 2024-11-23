import socket

# Create the target host and port via user input
target_host = input("What host would you like to target?: ")
target_port = input("What port would you like to target?: ")
target_port2 = int(target_port)

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sending data to the host
data_send = input("What data would you like to send to the server?: ")
client.sendto(data_send.encode(), (target_host, target_port2))

# Receive the response
data, addr = client.recvfrom(4096)

# Print out the response
print(response.decode())
client.close()

