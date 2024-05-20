import socket

port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

message_box = {}

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    command, mboxID, *message = msg.decode().split(maxsplit=2)
    
    if command == 'send':
        message = ' '.join(message)
        if mboxID not in message_box:
            message_box[mboxID] = []
        message_box[mboxID].append(message)
        response = 'OK'
    elif command == 'receive':
        if mboxID in message_box and message_box[mboxID]:
            response = message_box[mboxID].pop(0)
        else:
            response = 'No messages'
    elif command == 'quit':
        print('Server is shutting down.')
        break
    else:
        response = 'Invalid command'

    sock.sendto(response.encode(), addr)
