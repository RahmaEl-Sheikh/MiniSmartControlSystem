#169.254.223.222 
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('169.254.223.222', 5000))
client.send("I am CLIENT\n".encode())
from_server = client.recv(4096)
client.close()
print (from_server.decode())