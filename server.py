import socket
import threading


PORT = 2412
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
OTHERS = []

def SENDMSG(txt,new):
    for PERSON in OTHERS:
        if PERSON == new:
            pass
        else:
            PERSON.send(txt.encode(FORMAT))


def client_handle(conn, addr):
    print(f'[NEW CONNECTION] {addr} conneted')
    connected = True
    while connected:
        msg_length = conn.recv(2048).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                OTHERS.remove(conn)

            print(f'[{addr}] {msg}')
            SENDMSG(
                f'___________________________________________\n'
                f'[NEW MESSAGE]New message from {addr[0]} :\n{msg}\n'
                f'___________________________________________\n',conn)

    conn.close()

def start():
    server.listen()
    print(f'[LISTENING] Sever is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handle, args=(conn, addr))
        thread.start()
        OTHERS.append(conn)
        SENDMSG(f'___________________________________________\n'
                f'[NEW CONNECTION]{addr[0]} connected'
                f'\n___________________________________________\n', conn)
        print(f'\n[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

print('[STARTING] server is starting....')
start()
