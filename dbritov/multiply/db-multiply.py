import socket

s = socket.socket()
s.bind(('0.0.0.0', 9100))
s.listen(1)

conn,addr = s.accept()

print('Connected: {}'.format(addr))
print('format of accepted values is \'i_c\'')

while 1:
    data = conn.recv(1024)
    data.decode()
    a = data.decode()
    if data:
        x = a.split(" ")
        res = int(x[0]) * int(x[1])
        conn.send(str(res).encode())
        x = []
    else:
        print("Connection closed")
        break
s.close()
