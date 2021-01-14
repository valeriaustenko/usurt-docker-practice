import socket

s = socket.socket()

s.bind(('0.0.0.0',7575))
s.listen(1)

conn, addr = s.accept()

print ('connected:',format(addr))

while 1:
    x = conn.recv(1024)
    a = x.decode()
    if x:
        x = a.split(" ")
        y = float(x[0]) + float(x[1])
        conn.send(str(y).encode())
    else:
        break
s.close()
