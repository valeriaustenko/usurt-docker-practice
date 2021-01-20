import socket

massiv_2x = []
massiv_sin2x = []


s = socket.socket()
s.connect(('makhmat_server_2x', 9999))

for i in range(1,11):
    Z = 2
    x = str(i) + " " + str(Z)
    print("X"+str(i)+" = "+str(i))
    s.send(str(x).encode())
    massiv_2x.append(s.recv(1024).decode())
s.close()


s = socket.socket()
s.connect(('makhmat_server_sinx', 8888))

for i in range(10):
    s.send(str(massiv_2x[i]).encode())
    massiv_sin2x.append(s.recv(1024).decode())
s.close()


s = socket.socket()
s.connect(('makhmat_server_3x', 9999))

for i in range(10):
    Z = 3
    x = str(massiv_sin2x[i]) + " " + str(Z)
    s.send(str(x).encode())
    y = s.recv(1024).decode()
    print("Y"+str(i+1)+" = "+str(y))
s.close()
