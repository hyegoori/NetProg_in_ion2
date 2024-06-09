import socket
import select

HOST = ''
PORT = 2500
BUFSIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

client_sockets = []

print('서버 시작')

while True:
    read_sockets, _, exception_sockets = select.select([server_socket] + client_sockets, [], client_sockets)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            client_sockets.append(client_socket)
            print(f'새 클라이언트 접속: {client_address}')
        else:
            try:
                message = notified_socket.recv(BUFSIZE)
                if not message:
                    print(f'클라이언트 연결 종료: {notified_socket.getpeername()}')
                    client_sockets.remove(notified_socket)
                    notified_socket.close()
                    continue

                print(f'수신: {notified_socket.getpeername()} : {message.decode()}')

                for client_socket in client_sockets:
                    if client_socket != notified_socket:
                        client_socket.send(message)

            except Exception as e:
                print(f'에러: {e}')
                client_sockets.remove(notified_socket)
                notified_socket.close()
                continue

    for notified_socket in exception_sockets:
        client_sockets.remove(notified_socket)
        notified_socket.close()
