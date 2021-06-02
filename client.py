import socket
import os
import threading
import tkinter

def HOST():
    HOSTADDR = []
    DIALOG = tkinter.Tk()
    DIALOG.geometry('455x70')
    LABEL = tkinter.Label(DIALOG,text='What is the server IP?')
    INPUT1 = tkinter.Entry(DIALOG,width=40)
    BUTTON = tkinter.Button(DIALOG,text='Submit',width=7,height=1)
    LABEL.place(x=5,y=5)
    INPUT1.place(x=5,y=25)
    BUTTON.place(x=380,y=29)

    def BIND(event):
        TXT = INPUT1.get()
        HOSTADDR.append(TXT)
        DIALOG2 = tkinter.Tk()
        DIALOG2.geometry('455x70')
        LABEL = tkinter.Label(DIALOG2,text='What is the server PORT?')
        INPUT = tkinter.Entry(DIALOG2,width=40)
        BUTTON = tkinter.Button(DIALOG2,text='Submit',width=7,height=1)
        LABEL.place(x=5,y=5)
        INPUT.place(x=5,y=25)
        BUTTON.place(x=380,y=29)

        def PORT(event):
            TXT = int(INPUT.get())
            HOSTADDR.append(TXT)
            DIALOG2.quit()
            DIALOG2.destroy()

        BUTTON.bind('<ButtonRelease-1>',PORT)
        DIALOG2.mainloop()
        DIALOG.quit()
        DIALOG.destroy()
    
    
    BUTTON.bind('<ButtonRelease-1>',BIND)
    DIALOG.mainloop()

    return (HOSTADDR[0],HOSTADDR[1])


ADDR = HOST()
WORKING = True
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
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

def UI():
    WINDOW = tkinter.Tk()
    WINDOW.geometry('900x600')
    INPUT = tkinter.Entry(WINDOW,width=60)
    TEXTUSERS = tkinter.Text(WINDOW,width=28,height=37)
    TEXTUSERS.insert(tkinter.END,"There's No user in server")
    BUTTON = tkinter.Button(WINDOW,text='SEND!',width=10)

    BUTTON.place(x=570,y=553)
    TEXTUSERS.place(x=670,y=10)
    INPUT.place(x=10,y=550)

    WINDOW.mainloop()

UI()
while WORKING:
    MSG = input()
    send(MSG)
    if MSG == DISCONNECT_MESSAGE:
        WORKING = False
        exit()