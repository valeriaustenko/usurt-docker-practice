import socket

massiv = []

s = socket.socket()
s.connect(('sid_server_sinx', 9336))

for i in range(1,11):
    print("X"+str(i)+" = "+str(i))
    s.send(str(i).encode())
    massiv.append(s.recv(1024).decode())
s.close()

s = socket.socket()
s.connect(('sid_server_1x', 9339))

for i in range(10):
    s.send(str(massiv[i]).encode())
    y = s.recv(1024).decode()
    print("Y"+str(i+1)+" = 1/sin(X"+str(i+1)+") = 1/sin("+str(i+1)+") = "+str(y))
s.close()



