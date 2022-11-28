from concurrent.futures import thread
import socket
from threading import Thread
from tkinter import *
import random

from PIL import Image, ImageTk

list_of_clients = []
nickname_list = []
screen_width = None
screen_height = None
SERVER = None
PORT = None
IP_ADDRESS = None
playerName = None
canvas1 = None
nameEntry = None
nameWindow = None


def saveName():
    global playerName, SERVER, nameEntry, nameWindow
    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())


def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    nameWindow = Tk()
    nameWindow.title("TAMBOLA GAME")
    nameWindow.geometry("800x600")

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file="./assets/background.png")

    canvas1 = Canvas(nameWindow, width=500, height=500)
    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.create_text(screen_width/4.5, screen_height/8,
                        text="Enter your name", font=("Chalkboard SE", 60), fill='black')

    nameEntry = Entry(nameWindow, width=15, justify='center',
                      font=("Chalkboard SE", 30), bd=5, bg="white")
    nameEntry.place(x=screen_width/7, y=screen_height/5.5)

    button = Button(nameWindow, text="Save", command=saveName, font=(
        "Chalkboard SE", 30), bd=5, bg="white", width=11, height=2)
    button.place(x=screen_width/6, y=screen_height/4)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()


def receivedMsg():
    pass
    # conn.send('Welcome to tambola game! '.encode())
    # while True:
    #     try:
    #         message = conn.recv(2048).decode()
    #         if message:
    #             print(message)
    #             broadcast(message, conn)
    #         else:
    #             remove(conn)
    #             remove_nickname(nickname)
    #     except:
    #         continue


def setup():
    global SERVER, PORT, IP_ADDRESS
    IP_ADDRESS = '127.0.0.1'
    PORT = 5000

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=receivedMsg)
    thread.start()
    askPlayerName()


setup()
