import socket
import time

server_ip = 'localhost'
port = 3333
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((server_ip, port))

def send_message(message, address):
    reTx = 0
    while reTx <= 5:
        formatted_message = f"{reTx} {message}"
        sock.sendto(formatted_message.encode(), address)
        sock.settimeout(2)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            # ack를 수신했지만 출력하지 않음
            return reTx
        except socket.timeout:
            reTx += 1
            continue
    return -1

while True:
    msg = input('-> ')
    if msg == 'quit':
        break
    reTx = send_message(msg, (server_ip, port))
    sock.settimeout(None)
    response, _ = sock.recvfrom(BUFF_SIZE)
    print(f"<- {response.decode()}")

sock.close()

