import socket

s = socket.socket()

s.bind(('0.0.0.0',1111))
s.listen(1)

conn, addr = s.accept()

print ('connected:',format(addr))

while 1:
    x = conn.recv(1024)
    a = x.decode()
    if x:
        x = a.split(" ")
        y = int(x[0]) * int(x[1])
        conn.send(str(y).encode())
    else:
        break
s.close()
