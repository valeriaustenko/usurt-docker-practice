import socket

s = socket.socket()
s.bind(('0.0.0.0', 9500))
s.listen(1)

conn, addr = s.accept()

print('Connected: {}'.format(addr))

while 1:
    data = conn.recv(1024)
    data.decode()
    a = data.decode()
    if data:
        print("data = {}".format(data))
        x = a.split(" ")
        res = float(x[0]) / float(x[1])
        conn.send(str(res).encode())
        x = []
    else:
        print("No data. Connection closed")
        break
s.close()
