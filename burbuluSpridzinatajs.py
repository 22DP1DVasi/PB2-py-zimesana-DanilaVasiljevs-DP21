# Daņila Vasiļjevs DP2-1

from tkinter import *
from random import randint

GARUMS = 500
PLATUMS = 800   # loga izmēri

logs = Tk()
logs.title("Burbuļu spridzinātājs.")
a = Canvas(logs, width=PLATUMS, height=GARUMS, bg="darkblue")
a.pack()

kuga_id = a.create_polygon(5, 5, 5, 25, 30, 15, fill="red") # zemūdenes trijstūris
kuga_id2 = a.create_oval(0, 0, 30, 30, outline="red")       # zemūdenes riņķa līnijas
KUGA_R = 15     # zemūdenes rādiuss
VID_X = PLATUMS / 2
VID_Y = GARUMS / 2      # ekrāna centra koordinātas

a.move(kuga_id, VID_X, VID_Y)
a.move(kuga_id2, VID_X, VID_Y)  # pārvieto abas zemūdenes daļas uz ekrāna centru
KUGA_ATR = 10   # zemūdenes ātrums

def parvietot_kugi(notikums):
    if notikums.keysym == "Up":         # uz augšu
        a.move(kuga_id, 0, -KUGA_ATR)
        a.move(kuga_id2, 0, -KUGA_ATR)
    elif notikums.keysym == "Down":     # uz leju
        a.move(kuga_id, 0, KUGA_ATR)
        a.move(kuga_id2, 0, KUGA_ATR)
    elif notikums.keysym == "Left":     # pa kreisi
        a.move(kuga_id, -KUGA_ATR, 0)
        a.move(kuga_id2, -KUGA_ATR, 0)
    elif notikums.keysym == "Right":    # pa labi
        a.move(kuga_id, KUGA_ATR, 0)
        a.move(kuga_id2, KUGA_ATR, 0)

a.bind_all("<Key>", parvietot_kugi)

burb_id = list()          # saraksts burbuļu ID
burb_r = list()           # saraksts burbuļu rādiusiem
burb_atrums = list()      # saraksts burbuļu ātrumiem
MIN_BURB_R = 10
MAX_BURB_R = 30
MAX_BURB_ATR = 10
ATSTARPE = 100

def izveidot_burbuli():
    x = PLATUMS + ATSTARPE
    y = randint(0, GARUMS)
    r = randint(MIN_BURB_R, MAX_BURB_ATR)
    id1 = a.create_oval(x - r, y - r, x + r, y + r, outline="white")
    burb_id.append(id1)
    burb_r.append(r)
    burb_atrums.append(randint(1, MAX_BURB_ATR))

input()
