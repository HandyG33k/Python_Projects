import socket

# Create the target host and port via user input
target_host = input("What host would you like to target?: ")
target_port = input("What port would you like to target?: ")
target_port2 = int(target_port)

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the client 
client.connect((target_host, target_port2))

# Sending data to the host
data_send = input("What data would you like to send to the server?: ")
data_send = data_send.replace(r"\r\n", "\r\n")
data_send2 = data_send.encode()

client.send(data_send2)

# Receive the response
response = client.recv(4096)

# Print out the response
print(response.decode())
client.close()
