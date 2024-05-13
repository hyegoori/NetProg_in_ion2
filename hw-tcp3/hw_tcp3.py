from socket import *

def send_not_found(conn):
    conn.send(b'HTTP/1.1 404 Not Found\r\n')
    conn.send(b'\r\n')
    conn.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>')

def handle_request(filename, conn):
    # 파일 확장자에 따른 MIME 타입 설정
    if filename.endswith('.html'):
        mimeType = 'text/html; charset=utf-8'  # charset=utf-8 추가
        mode = 'r'
        encoding = 'utf-8'
    elif filename.endswith('.png'):
        mimeType = 'image/png'
        mode = 'rb'
    elif filename.endswith('.ico'):
        mimeType = 'image/x-icon'
        mode = 'rb'
    else:
        send_not_found(conn)
        return
    
    # 파일 존재 여부 확인 및 전송
    try:
        with open(filename, mode, encoding=encoding if 'encoding' in locals() else None) as f:
            data = f.read()
            conn.send(b'HTTP/1.1 200 OK\r\n')
            conn.send('Content-Type: '.encode() + mimeType.encode() + b'\r\n')
            conn.send(b'\r\n')
            if isinstance(data, str):
                conn.send(data.encode('utf-8'))  # UTF-8로 인코딩 변경
            else:
                conn.send(data)  # 바이너리 파일의 경우
    except FileNotFoundError:
        send_not_found(conn)


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 80))
    s.listen(10)
    print("서버가 실행되었습니다.")

    while True:
        c, addr = s.accept()
        data = c.recv(1024)
        msg = data.decode()
        req = msg.split('\r\n')[0]  # 요청 라인 추출
        filename = req.split(' ')[1][1:]  # 요청된 파일 이름 추출
        
        if filename == '':  # 기본 페이지 설정
            filename = 'index.html'
        
        handle_request(filename, c)
        c.close()

if __name__ == '__main__':
    main()
