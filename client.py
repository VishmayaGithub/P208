
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


def musicWindow():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")


    window = Tk()
    window.title("Music Window")
    window.geometry("330x390")
    window.configure(bg="LightSkyBlue")

    selectLabel = Label(window, text="Select Song", bg="LightSkyBlue" ,font=("Calibri",10))    
    selectLabel.place(x=5,y=3)

    listBox = Listbox(window,height=10,width=33,activestyle="dotbox",font=("Calibri",13),bd=1,bg="LightSkyBlue")
    listBox.place(x=10,y=24)

    scrollbar1= Scrollbar(listBox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listBox.yview)

    PlayButton = Button(window,text="Play",bd=1,font=("Calibri",11),bg="SkyBlue", width=10)
    PlayButton.place(x=30,y=270)

    Stop = Button(window,text="Stop",bd=1,font=("Calibri",11),bg="SkyBlue", width=10)
    Stop.place(x=200,y=270)

    Upload = Button(window,text="Upload",bd=1,font=("Calibri",11),bg="SkyBlue", width=10)
    Upload.place(x=30,y=320)

    Download = Button(window,text="Download",bd=1,font=("Calibri",11),bg="SkyBlue", width=10)
    Download.place(x=200,y=320)

    infoLabel = Label(window, text="", bg="blue" ,font=("Calibri",8))    
    infoLabel.place(x=4,y=270)

    window.mainloop()






def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()
