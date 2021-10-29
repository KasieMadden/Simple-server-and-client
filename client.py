import socket
target_host = "127.0.0.1"
target_port = 27700


#promt user
messIn = input("Enter a string: ")
# create a socket connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# let the client connect
client.connect((target_host, target_port))

# send some data
client.send(str(messIn).encode())

# get reversed string  data
response = client.recv(4096).decode()

print("String reversed: " + response)
client.close()
