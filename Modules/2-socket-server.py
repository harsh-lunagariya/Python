# socket() use for creating socket
# bind()  use for bind the ip address and port number
# listen()  how many request it listen
# accept()  accept the user return user and address of it
# recv().decode()  recive messsage from the user and decode it
# send(bytes("",'utf-8'))  send the message to each other


import socket
import struct

s = socket.socket()
print('socket Created')

s.bind(('192.168.1.6',9999))

s.listen(3)
print('waiting for connections')

def send_img(conn,path):
    with open(path,'rb') as f:
        data = f.read()
    
    size = len(data)

    c.sendall(struct.pack('!I',size))
    c.sendall(data)
    print("Image send successfully!!")


while True:
    c,add = s.accept()
    name = c.recv(1024).decode()
    print("connected with",add,name)

    with c:
        send_img(c,'img.jpg')

    c.close()