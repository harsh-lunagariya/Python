import socket
import struct

def revimage(sock,file):
    data = sock.recv(4)
    if not data:
        print("not received")
        return
    size = struct.unpack('!I',data)[0]
    data = b''
    while len(data)<size:
        packet = sock.recv(4096)
        if not packet:
            break
        data += packet
        
    with open("imj.jpg","wb") as f:
        f.write(data)
    print("image saved")

c = socket.socket()

c.connect(('192.168.1.6',9999))

name = input("Enter your name : ")
c.send(bytes(name,'utf-8'))

revimage(c,"img.jpg")