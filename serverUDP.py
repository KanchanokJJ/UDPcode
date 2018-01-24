import socket
def num(s):
    try:
        return int(s)
    except ValueError:
        return -1

UDP_IP = '127.0.0.1'
UDP_PORT = 5011
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = num(data)
    Result = 1
    if data == -1:
        sock.sendto("Fail Number", addr)
    elif data<0:
        sock.sendto("Number Not Negative Number", addr)
    else:
        for x in range(1, data+1):
            Result *=x
        sock.sendto(str(Result), addr)
        print "Received Result:", Result

