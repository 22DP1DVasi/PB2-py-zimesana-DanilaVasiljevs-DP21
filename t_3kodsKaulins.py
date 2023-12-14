# Daņila Vasiļjevs DP2-1

from tkinter import *
from random import randint

def ripinat():
    teksts.delete(0.0, END)
    teksts.insert(END, str(randint(1, 6)))

logs = Tk()
teksts = Text(logs, width=1, height=1)
pogaA = Button(logs, text="Klikšķini, lai ripinātu!", command=ripinat)
teksts.pack()
pogaA.pack()
input()
