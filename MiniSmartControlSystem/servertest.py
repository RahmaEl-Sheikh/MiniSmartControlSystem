#169.254.223.222
import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('169.254.223.222', 5000))
serv.listen(5)
while True:
  conn, addr = serv.accept()
  from_client = ''
  while True:
    data = conn.recv(4096)
    if not data: break
    from_client += data.decode('utf8')
    print (f'From client: {from_client}')
    conn.send("I am SERVER\n".encode())
  conn.close()
print ('client disconnected and shutdown')