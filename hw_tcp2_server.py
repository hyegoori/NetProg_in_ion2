import socket

def calculate(expression):
    try:
        # 공백 제거
        expression = expression.replace(" ", "")
        # 연산자와 피연산자 분리
        for op in ('+', '-', '*', '/'):
            if op in expression:
                operands = expression.split(op)
                operand1, operand2 = map(float, operands)  # 소수점 계산을 위해 float 사용
                if op == '+':
                    return str(operand1 + operand2)
                elif op == '-':
                    return str(operand1 - operand2)
                elif op == '*':
                    return str(operand1 * operand2)
                elif op == '/':
                    return str(round(operand1 / operand2, 1))  # 소수점 첫째 자리까지 표시
    except Exception as e:
        return "Error: 잘못된 식"

def main():
    host = ''  # 모든 인터페이스에서 접속 허용
    port = 3333  # 클라이언트와 동일한 포트 사용

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("서버 시작, 클라이언트의 연결을 기다립니다...")
        conn, addr = s.accept()
        with conn:
            print(f"{addr}에서 연결되었습니다.")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                expression = data.decode()
                result = calculate(expression)
                conn.sendall(result.encode())

if __name__ == "__main__":
    main()
