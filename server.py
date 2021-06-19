  
import socket
s=socket.socket()
s.bind(('localhost',1234))
s.listen()
while True:
    c, addr = s.accept()

    while True:
        a = input("enter msg:")
        c.send(bytes(a, encoding='utf-8'))
        msg = c.recv(1024)
        print("clientmsg:", msg)
