import socket
c=socket.socket()
c.connect(('localhost',1234))
while True:
        print(c.recv(1024))
        ms = input("enter msg:")
        c.send(bytes(ms, encoding='utf-8'))
