import socket

s = socket.socket()
s1 = socket.socket()
s2 = socket.socket()
result_of_mult = []
result_of_mult_2 = []
result_of_summ = []


s.connect(('as-multiply', 9500))
for i in range(1, 11):
    c = 2
    args = str(i) + " " + str(c)
    s.send(args.encode())
    args = ""
    result_of_mult.append(s.recv(1024).decode())

for i in range(10):
    print(result_of_mult[i])

for i in range(1, 11):
    args = str(i) + " " + str(i)
    s.send(args.encode())
    args = ""
    result_of_mult_2.append(s.recv(1024).decode())
s.close()
for i in range(10):
    print(result_of_mult_2[i])	



s1.connect(('as-summ', 9501))
for i in range(10):
    args = str(result_of_mult[i] + " " + result_of_mult_2[i])
    s1.send(args.encode())
    args = ""
    result_of_summ.append(s1.recv(1024).decode())
s1.close()
for i in range(10):
    print(result_of_summ[i])
	


s2.connect(('as-sub', 9502))
for i in range(10):
    args = str(result_of_summ[i] + " " + "1")
    s2.send(args.encode())
    result = s2.recv(1024).decode()
    print("Function 2x + x^2 - 1 = {}".format(result))
    args = ""
s2.close()
