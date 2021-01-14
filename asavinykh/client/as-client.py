import socket

s = socket.socket()
s.connect(('as-server', 9500))

for i in range(10):
    c = 2
    arg = str(i) + " " + str(c)
    s.send(arg.encode())
    arg = ""
    print(s.recv(1024).decode())
s.close()
