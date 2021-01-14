import socket

s = socket.socket()
s1 = socket.socket()
s2 = socket.socket()

result_of_diff = []
result_of_mult = []


s.connect(('ay-diff', 9200))
for i in range(1, 11):
    c = 1
    args = str(c) + " " + str(i)
    s.send(args.encode())
    args = ""
    result_of_diff.append(s.recv(1024).decode())
s.close()

for i in range(10):
    print(result_of_diff[i])



s1.connect(('ay-mult', 9201))
for i in range(10):
    args = str(result_of_diff[i]) + " " + str(i + 1) 
    s1.send(args.encode())
    result_of_mult.append(s1.recv(1024).decode())
s1.close()

for i in range(10):
    print(result_of_mult[i])



s2.connect(('ay-expon', 9203))
for i in range(10):
    s2.send(result_of_mult[i].encode())
    result = s2.recv(1024).decode()
    print("Result of function exp(-(x-1)*x) equals = {0}".format(result))
s2.close()
