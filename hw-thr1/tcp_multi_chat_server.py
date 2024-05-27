import socket
import threading

clients = {}
lock = threading.Lock()

def client_handler(conn, addr):
    print(f"{addr} connected.")
    try:
        nickname = conn.recv(1024).decode()
        with lock:
            clients[conn] = nickname

        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = f"{nickname}: {data.decode()}"
            print(message)
            with lock:
                for client in clients:
                    if client != conn:
                        client.send(message.encode())
    finally:
        with lock:
            print(f"{nickname} disconnected.")
            del clients[conn]
        conn.close()

def main():
    host = '0.0.0.0'
    port = 2500

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is listening...")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=client_handler, args=(conn, addr))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    main()


