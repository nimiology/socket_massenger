mport socket
import os
import threading


WORKING = True
SERVER = input('What is the server IP?')
PORT = int(input('What is the server PORT?'))
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
print('[CONNECTION] connected successfully')

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(2048 - len(send_length))
    client.send(send_length)
    client.send(message)





def RECIVER():
    while WORKING:
        DATA = client.recv(2048).decode(FORMAT)
        print(DATA)

print(f"if you want to exit type : {DISCONNECT_MESSAGE}")
THREAD = threading.Thread(target=RECIVER)
THREAD.start()
while WORKING:
    MSG = input()
    send(MSG)
    if MSG == DISCONNECT_MESSAGE:
        WORKING = False
        exit()
