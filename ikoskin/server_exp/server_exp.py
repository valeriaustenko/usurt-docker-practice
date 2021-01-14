import socket
import math

s = socket.socket()
s.bind(('0.0.0.0', 8665))
s.listen(1)

conn, addr = s.accept()

print('Connected: {}'.format(addr))
print('function exp(x)')

while 1:
        exp = conn.recv(1024)
        exp.decode()
        arg = float(exp.decode())
        if data:
                arg = math.exp(arg)
                conn.send(str(arg).encode())
        else:
             break
s.close()

