import socket

massiv = []

s = socket.socket()
s.connect(('ikoskin_server_sinx', 8664))

for i in range(1,11):
    print("X"+str(i)+" = "+str(i))
    s.send(str(i).encode())
    massiv.append(s.recv(1024).decode())
s.close()

s = socket.socket()
s.connect(('ikoskin_server_plus', 8866))

for i in range(10):
    x = str(massiv[i]) + " " + str(i+1)
    s.send(str(x).encode())
    y = s.recv(1024).decode()
    print("Y"+str(i+1)+" = "+str(y))
s.close()
