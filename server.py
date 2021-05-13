import socket
import threading

HEADER = 64
PORT = 241
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONECT"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
OTHERS = []


def client_handle(conn, addr):
    print(f'[NEW CONNECTION] {addr} conneted')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'[{addr}] {msg}')

            for PERSON in OTHERS:
                if PERSON == conn:
                    PERSON.send(f'[{addr}]   {msg}'.encode(FORMAT))
                else:
                    PERSON.send(f'[{addr}]   {msg}'.encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f'[LISTENING] Sever is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handle, args=(conn, addr))
        thread.start()
        OTHERS.append(conn)
        print(f'\n[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

print('[STARTING] server is starting....')
start()