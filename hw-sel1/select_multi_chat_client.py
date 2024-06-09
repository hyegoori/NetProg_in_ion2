import socket
import threading

def receive(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            print("Disconnected from server.")
            sock.close()
            break

def main():
    host = 'localhost'
    port = 2500

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        nickname = input("Enter your nickname: ")
        sock.sendall(nickname.encode())
        print("Connected to the server.")

        thread = threading.Thread(target=receive, args=(sock,))
        thread.daemon = True
        thread.start()

        while True:
            message = input()
            if message == 'quit':
                break
            sock.sendall(message.encode())

if __name__ == "__main__":
    main()
