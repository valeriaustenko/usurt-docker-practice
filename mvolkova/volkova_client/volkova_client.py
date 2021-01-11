import socket

massiv = []

s = socket.socket()
s.connect(('volkova_server_stepenp', 6969))

for i in range(1,11):
    P = 2
    x = str(i) + " " + str(P)
    print("X"+str(i)+" = "+str(i))
    s.send(str(x).encode())
    massiv.append(s.recv(1024).decode())
s.close()


s = socket.socket()
s.connect(('volkova_server_dobavlenie_constanti', 9696))
for i in range(10):
    C = "-2"
    x = str(massiv[i]) + " " + str(C)
    s.send(str(x).encode())
    y = s.recv(1024).decode()
    print("Y = " + str(y))
s.close()
