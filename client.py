import socket
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image

leftBoxes=[]
rightBoxes=[]

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None
canvas2 = None
playerName = None
nameEntry = None
nameWindow = None
gameWindow = None


def finishingBox():
    global gameWindow
    global finishingbox
    global screen_width
    global screen_height

    finishingbox=Label(gameWindow,text="Home",font=("Helvetica",30),width=8,height=4,relief="ridge",borderwidth=0,bg="#800080",fg="#ffffff")
    finishingbox.place(x=screen_width/2-68,y=screen_height/2-160)

def leftBoard():
    global gameWindow
    global leftBoxes
    global screen_height

    xpos=30
    for box in range(0,11):
        if(box==0):
            boxLabel=Label(gameWindow,font=("Helvetica",30),width=2,height=1,relief="ridge",borderwidth=0,bg="#ff0000")
            boxLabel.place(x=xpos,y=screen_height/2-88)
            leftBoxes.append(boxLabel)
            xpos+=50
        else:
            boxLabel=Label(gameWindow,font=("Helvetica",55),width=2,height=1,relief="ridge",borderwidth=0,bg="#ffffff")
            boxLabel.place(x=xpos,y=screen_height/2-100)
            leftBoxes.append(boxLabel)
            xpos+=75

def rightBoard():
    global gameWindow
    global rightBoxes
    global screen_height

    xpos=850
    for box in range(0,11):
        if(box==10):
            boxLabel=Label(gameWindow,font=("Helvetica",30),width=2,height=1,relief="ridge",borderwidth=0,bg="#00ff00")
            boxLabel.place(x=xpos,y=screen_height/2-88)
            rightBoxes.append(boxLabel)
            xpos+=50
        else:
            boxLabel=Label(gameWindow,font=("Helvetica",55),width=2,height=1,relief="ridge",borderwidth=0,bg="#ffffff")
            boxLabel.place(x=xpos,y=screen_height/2-100)
            rightBoxes.append(boxLabel)
            xpos+=75

def gamewindow():
    global gameWindow
    global canvas2
    global screen_width
    global screen_height
    global dice

    gameWindow = Tk()
    gameWindow.title("Ludo")
    gameWindow.attributes("-fullscreen", True)
    screen_width = gameWindow.winfo_screenwidth()
    screen_height = gameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file="./assets/background.png")

    canvas2 = Canvas(gameWindow, width=500, height=500)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg, anchor="nw")
    canvas2.create_text(screen_width/2, screen_height/5,
    text="Ludo", font=("Chalkboard SE", 100), fill="#ffffff")

    leftBoard()
    rightBoard()
    finishingBox()
    gameWindow.resizeable(True, True)
    gameWindow.mainloop()


def saveName():
    global SERVER
    global nameWindow
    global playerName
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())
    gamewindow()


def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow = Tk()
    nameWindow.title("Ludo")
    nameWindow.attributes("-fullscreen", True)
    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file="./assets/background.png")

    canvas1 = Canvas(nameWindow, width=500, height=500)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.create_text(screen_width/2, screen_height/5, text="Enter Name", font=("Chalkboard SE", 100), fill="#ffffff")

    nameEntry = Entry(nameWindow, width=15, justify="center", font=("Chalkboard SE", 50), bd=5, bg="#ffffff")
    nameEntry.place(x=screen_width/2-220, y=screen_height/4+100)

    button = Button(nameWindow, text="save", font=("chalkboard SE", 30), width=15, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x=screen_width/2-130, y=screen_height/2-30)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    # Creating First Window
    askPlayerName()


setup()
