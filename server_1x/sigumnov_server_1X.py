import socket

s = socket.socket()

s.bind(('0.0.0.0',9339))
s.listen(1)

conn, addr = s.accept()

print ('connected:',format(addr))

while 1:
    x = conn.recv(1024)
    if x:
        x = float(x.decode())
        x = str(1/x)
        conn.send(x.encode())
    else:
        break
s.close()
