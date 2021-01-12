import socket

massiv_2x = []
massiv_sinx = []
massiv_cosx = []


s = socket.socket()
s.connect(('kguz_server_2x', 7373))

for i in range(1,11):
    Z = 2
    x = str(i) + " " + str(Z)
    print("X"+str(i)+" = "+str(i))
    s.send(str(x).encode())
    massiv_2x.append(s.recv(1024).decode())
s.close()


s = socket.socket()
s.connect(('kguz_server_sinx', 7272))
for i in range(10):
    s.send(str(massiv_2x[i]).encode())
    massiv_sinx.append(s.recv(1024).decode())
s.close()


s = socket.socket()
s.connect(('kguz_server_cosx', 7474))
for i in range(10):
    s.send(str(massiv_2x[i]).encode())
    massiv_cosx.append(s.recv(1024).decode())
s.close()


s = socket.socket()
s.connect(('kguz_server_plus', 7575))

for i in range(10):
    x = str(massiv_sinx[i]) + " " + str(massiv_cosx[i])
    s.send(str(x).encode())
    y = s.recv(1024).decode()
    print("Y = " + y)
s.close()

