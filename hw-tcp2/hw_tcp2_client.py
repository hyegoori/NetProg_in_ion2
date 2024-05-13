import socket

def main():
    host = 'localhost'  
    port = 3333  

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input("계산식 입력 ('q' 입력시 종료): ")
            if message.lower() == 'q':
                break
            s.sendall(message.encode())
            result = s.recv(1024)
            print("계산 결과:", result.decode())

if __name__ == "__main__":
    main()
