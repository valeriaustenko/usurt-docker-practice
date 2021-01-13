import socket

s = socket.socket()
s1 = socket.socket()
s2 = socket.socket()
result_of_mult = []
result_of_exp = []
result_of_summ = []

 
s.connect(('db-multiply', 9100))
for i in range(1, 11):
    c = 2
    args = str(i) + " " + str(c)
    s.send(args.encode())
    args = ""
    result_of_mult.append(s.recv(1024).decode())
s.close()
for i in range(10):
    print(result_of_mult[i])



s1.connect(('db-expon', 9101))
for i in range(10):
    s1.send(result_of_mult[i].encode())
    result_of_exp.append(s1.recv(1024).decode())
s1.close()

for i in range(10):
    print(result_of_exp[i])



s2.connect(('db-summ', 9102))
for i in range(10):
    args = str(result_of_mult[i])+ " " + str(result_of_exp[i])
    s2.send(args.encode())
    result = s2.recv(1024).decode()
    b = i + 1
    print("Function 2*x + exp(2x) at x = {0} equals = {1}".format(b, round(float(result), 2)))
    result_of_summ.append(round(float(result), 2))
    args = ""
s2.close()


import matplotlib.pyplot as plt
  
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = result_of_summ

plt.title("Функция y = 2*x + exp(2x) при x = (1 .. 10)")
plt.xlabel("x")
plt.ylabel("y = 2x + exp(x)")
plt.grid(True)
plt.plot(x, y)
plt.savefig("/common/pic.png")
