# Daņila Vasiļjevs DP2-1

from tkinter import *

def Adarbiba():
    print("Paldies!")

def Bdarbiba():
    print("Au! Man sāp!")

logs = Tk()
pogaA = Button(logs, text="Klikšķini te!", command=Adarbiba)
pogaB = Button(logs, text="Neklikšķini te!", command=Bdarbiba)
pogaA.pack()
pogaB.pack()
input()
