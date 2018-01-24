import socket
UDP_IP = '127.0.0.1'
UDP_PORT = 5011
while True:
    x = input("Enter a number: ")
    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
    sock.sendto(str(x), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "Result:", data
