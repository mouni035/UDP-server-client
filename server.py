import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip=''
s.bind((server_ip,9999))
print("UDP is listening")
while True:
    data, client_addr = s.recvfrom(1024)
    print(f"recevied '{data.decode}' from {client_addr}")
    reply=input("received msg")
    s.sendto(reply.encode(), client_addr)

          





