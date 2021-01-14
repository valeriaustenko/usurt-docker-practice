import socket

massiv_xxx = []
massiv_xx = []
massiv_3xx = []
massiv_sum = []

s = socket.socket()
s.connect(('purgina_server_stepen_p', 6666))

for i in range(1,11):
    P = 3
    x = str(i) + " " + str(P)
    print("X"+str(i)+" = "+str(i))
    s.send(str(x).encode())
    massiv_xxx.append(s.recv(1024).decode())


for i in range(1,11):
    P = 2
    x = str(i) + " " + str(P)
    s.send(str(x).encode())
    massiv_xx.append(s.recv(1024).decode())
s.close()


s = socket.socket()
s.connect(('purgina_server_3x', 1111))
for i in range(10):
    c = 3
    x = str(massiv_xx[i]) + " " + str(c)
    s.send(str(x).encode())
    massiv_3xx.append(s.recv(1024).decode())
s.close()


s = socket.socket()
s.connect(('purgina_server_plus', 4444))
for i in range(10):
    x = str(massiv_xxx[i]) + " -" + str(massiv_3xx[i])
    s.send(str(x).encode())
    massiv_sum.append(s.recv(1024).decode())


for i in range(10):
    k = 1
    x = str(massiv_sum[i]) + " " + str(k)
    s.send(str(x).encode())
    y = s.recv(1024).decode()
    print("Y = " + y)
s.close()
