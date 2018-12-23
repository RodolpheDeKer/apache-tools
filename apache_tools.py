#! /usr/bin/python3.6
#  -*- UTF8 -*-
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog
import sys
import os
########################################################################################################################
main = Tk()
main.geometry("1000x700+200+200")
main.title("Apache2 tools")
########################################################################################################################
def clavier(event):
    touche = event.keysym
    if touche == "Escape":
        quit(main)

def start_apach():
    os.system("/etc/init.d/apache2 start")
    messagebox.showinfo("Apache", "apache est mi en route")

def install_apach():
    os.system("sudo apt-get install apache2")
    messagebox.showinfo("Apache", "apache est installer")

def arr_apach():
    os.system("/etc/init.d/apache2 stop")
    messagebox.showinfo("Apache", "apache est arreter")
    ########################################################################################################################
bouton_install = Button(text="installer apache", command=install_apach).pack()
bouton_start = Button(text="Start Apache", command=start_apach).pack()
bouton_arreter = Button(text="arreter Apache", command=arr_apach).pack()

canvas = Canvas(main, width=0, height=0)
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()
########################################################################################################################
mainloop()