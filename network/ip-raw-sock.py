from socket import *
import os
import struct

def parsing(host):
    if os.name == 'nt':
        socket_protocol = IPPROTO_IP
    else:
        socket_protocol = IPPROTO_ICMP

    sock = socket(AF_INET, SOCK_RAW, socket_protocol)
    sock.bind((host, 0))
    
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
    
    if os.name == 'nt':
        sock.ioctl(SIO_RCVALL, RCVALL_ON)
    
    packet_number = 0
    try:
        while True:
            packet_number += 1
            data = sock.recvfrom(65535)
            ip_headers, ip_payloads = parse_ip_header(data[0])
            print(f"{packet_number}th packet\n")
            print("Version: ", ip_headers[0] >> 4) # 왼쪽 4bits에 해당하는 값
            print("Header Length: ", ip_headers[0] & 0x0f) # 오른쪽 4bits에 해당하는 값
            print("Type of Service: ", ip_headers[1])
            print("Total Length: ", ip_headers[2])
            print("Identification: ", ip_headers[3])
            print("IP Flags, Fragment Offset: ", flags_and_offset(ip_headers[4]))
            print("Time to Live: ", ip_headers[5])
            print("Protocol: ", ip_headers[6])
            print("Checksum: ", ip_headers[7])
            print("Source IP: ", inet_ntoa(ip_headers[8])) # byte -> IP
            print("Destination IP: ", inet_ntoa(ip_headers[9]))
            print("="*50)
    except KeyboardInterrupt:
            if os.name == 'nt':
                sock.ioctl(SIO_RCVALL, RCVALL_OFF)
                sock.close()

def parse_ip_header(ip_header):
    ip_headers = struct.unpack("!BBHHHBBH4s4s", ip_header[0:20])
    ip_payloads = ip_header[20:]
    return ip_headers, ip_payloads

# 숫자 -> byte -> bit
def flags_and_offset(int_num):
    byte_num = int_num.to_bytes(2, byteorder='big') # 2bytes 길이의 Big Endian 방식
    x = bytearray(byte_num)
    flags_and_flagment_offset = bin(x[0])[2:].zfill(8) + bin(x[1])[2:].zfill(8) # zfill(자릿수) 8자리
    return (flags_and_flagment_offset[:3], flags_and_flagment_offset[3:])
    
    
if __name__ == "__main__":
    host = "#" # 본인 IP
    print(f"Listening at [{host}]")
    parsing(host)
