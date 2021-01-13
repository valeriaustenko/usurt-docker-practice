import socket
import math

s = socket.socket()
s.bind(('0.0.0.0', 9203))
s.listen(1)

conn, addr = s.accept()

print('Connected: {}'.format(addr))

while 1:
    data = conn.recv(1024)
    data.decode()
    arg = int(data.decode())
    if data:
        arg = math.exp(arg)
        conn.send(str(arg).encode())
    else:
        print("No data. Connection closed")
        break
s.close()
