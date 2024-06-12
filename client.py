import socket
c= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = ('', 9999)
while True:
    msg=input("enter msg: ",)
    c.sendto(msg.encode(), s)
    reply, s= c.recvfrom(1024)