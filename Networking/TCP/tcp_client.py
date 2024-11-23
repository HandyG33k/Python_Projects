import socket

# Create the target host and port via user input
target_host = input("What host would you like to target?: ")
target_port = input("What port would you like to target?: ")

# Create a socket object
client = socket.socket(socket.AF_INT, socket.SOCK_STREAM)

# Connecting to the client 
client.connect((target_host, target_port))

# Sending data to the host
data_send = input("What data would you like to send to the client?: ")
client.send(data_send.encode())

# Receive the response
response = client.recv(4096)

# Print out the response
print(response.decode())
client.close()
