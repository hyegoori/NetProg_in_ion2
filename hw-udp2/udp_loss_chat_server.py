import socket
import random

port = 3333
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    message = data.decode()

    reTx = message.split(' ', 1)[0]
    if random.random() <= 0.5:
        continue
    else:
        sock.sendto(b'ack', addr)
        print(f"<- {reTx} {message.split(' ', 1)[1]}")

        response = input(f"-> ")
        formatted_response = f"{reTx} {response}"
        sock.sendto(formatted_response.encode(), addr)
