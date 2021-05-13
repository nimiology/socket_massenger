import socket
import os
import threading

HEADER = 64
PORT = 241
SERVER = '192.168.43.128'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONECT"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
print('[CONNECTION] connected successfully')

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def RECIVER():
    while True:
        DATA = client.recv(2048).decode(FORMAT)
        print(DATA)

print("if you want to exit type : !DISCONNECT")
THREAD = threading.Thread(target=RECIVER)
THREAD.start()
while True:
    MSG = input()
    send(MSG)