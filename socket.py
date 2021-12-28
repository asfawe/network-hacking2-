from socket import *
import os


def parsing(host):
    # raw socket 생성 및 bind
    if os.name == "nt":
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP
    sock = socket(AF_INET, SOCK_RAW, sock_protocol)
    sock.bind((host, 0))

    # socket 옵션
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    # promiscuous mode
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_ON)

    data = sock.recv(1024)
    print(data)

    # promiscuous mode 끄기
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_OFF)

    # 소켓 종료
    sock.close()


if __name__ == "__main__":
    host = "127.0.0.1"
    print(f"Listening at [{host}]")
    parsing(host)
