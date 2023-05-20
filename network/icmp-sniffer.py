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
            if ip_headers[6] == 1: # icmp
                ip_source_address = inet_ntoa(ip_headers[8])
                ip_destination_address = inet_ntoa(ip_headers[9])
                print(f"{ip_source_address} -> {ip_destination_address}")
                icmp_headers, icmp_payloads = parse_icmp_header(ip_payloads)
                # icmp header type
                if icmp_headers[0] == 0:
                    print("Echo Reply")
                elif icmp_headers[0] == 8:
                    print("Echo Request")
                print("icmp_headers => ", icmp_headers)
                print("icmp payloads => ", icmp_payloads)
                print("="*50)
    except KeyboardInterrupt:
            if os.name == 'nt':
                sock.ioctl(SIO_RCVALL, RCVALL_OFF)

def parse_ip_header(ip_header):
    ip_headers = struct.unpack("!BBHHHBBH4s4s", ip_header[0:20])
    ip_payloads = ip_header[20:]
    return ip_headers, ip_payloads

def parse_icmp_header(icmp_data):
    icmp_headers = struct.unpack("!BBHHH", icmp_data[:8])
    icmp_payloads = icmp_data[8:]
    return icmp_headers, icmp_payloads
    
if __name__ == "__main__":
    host = "#" # 본인 IP
    print(f"START SNIFFING at {host}")
    parsing(host)
