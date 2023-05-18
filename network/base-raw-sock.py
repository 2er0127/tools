from socket import *
import os

def parsing(host):
    # 운영체제가 윈도우일 경우
    if os.name == 'nt':
        socket_protocol = IPPROTO_IP
    else:
        socket_protocol = IPPROTO_ICMP
    sock = socket(AF_INET, SOCK_RAW, socket_protocol)
    sock.bind((host, 0))
    
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1) # IP_HDRINCL: IP 헤더 포함 옵션, 1: True
    
    # 윈도우의 Promiscuous Mode 활성화
    if os.name == 'nt':
        sock.ioctl(SIO_RCVALL, RCVALL_ON)
    
    data = sock.recvfrom(65535)
    print(data[0])
    
    # 윈도우의 Promiscuous Mode 종료
    if os.name == 'nt':
        sock.ioctl(SIO_RCVALL, RCVALL_OFF)
        
    sock.close()
    
if __name__ == "__main__":
    host = "#" # 본인 IP
    print(f"Listening at [{host}]")
    parsing(host)
