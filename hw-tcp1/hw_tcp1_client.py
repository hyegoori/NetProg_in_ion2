import socket
import struct  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

name = 'Hye Won Kim' 
sock.send(name.encode())


student_id_data = sock.recv(4) 
student_id = struct.unpack('!I', student_id_data)[0] 
print(f'Received Student ID: {student_id}')

sock.close()
