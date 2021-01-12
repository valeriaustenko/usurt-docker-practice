import socket
import math

s = socket.socket()

s.bind(('0.0.0.0',8785))
s.listen(1)

conn, addr = s.accept()

print ('connected:',format(addr))

while 1:
    x = conn.recv(1024)
    a = x.decode()
    if x:
        x = a.split(" ")
        y = math.log(int(x[0]),int(x[1]))
        conn.send(str(y).encode())
    else:
        break
s.close()
