import socket
import math

s = socket.socket()

s.bind(('0.0.0.0',7272))
s.listen(1)

conn, addr = s.accept()

print ('connected:',format(addr))

while 1:
    x = conn.recv(1024)
    if x:
        x = int(x.decode())
        x = str(math.sin(x))
        conn.send(x.encode())
    else:
        break
s.close()
