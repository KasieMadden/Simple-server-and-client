import socket

bind_ip = "127.0.0.1"
bind_port = 27700

#Reverse function 
def messRev(s):
	return s[::-1]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(1)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))

client, addr = server.accept()
print("[*] Accepted connection from: %s:%d" + str(addr))

#while True:
mess = client.recv(4096).decode('utf-8')
#if not mess:
#	exit	
print("Message recived: " + str(mess))
client.send(messRev(mess).encode())

client.close()
	
