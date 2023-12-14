# Daņila Vasiļjevs DP2-1

from tkinter import *
from random import randint
from time import sleep
from math import sqrt

# 1. solis
GARUMS = 500
PLATUMS = 800   # loga izmēri

logs = Tk()
logs.title("Burbuļu spridzinātājs.")
a = Canvas(logs, width=PLATUMS, height=GARUMS, bg="darkblue")
a.pack()

# 2. solis
kuga_id = a.create_polygon(5, 5, 5, 25, 30, 15, fill="red") # zemūdenes trijstūris
kuga_id2 = a.create_oval(0, 0, 30, 30, outline="red")       # zemūdenes riņķa līnijas
KUGA_R = 15     # zemūdenes rādiuss
VID_X = PLATUMS / 2
VID_Y = GARUMS / 2      # ekrāna centra koordinātas

a.move(kuga_id, VID_X, VID_Y)
a.move(kuga_id2, VID_X, VID_Y)  # pārvieto abas zemūdenes daļas uz ekrāna centru

# 3. solis
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

# 4. solis
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
    r = randint(MIN_BURB_R, MAX_BURB_R)
    id1 = a.create_oval(x - r, y - r, x + r, y + r, outline="white")
    burb_id.append(id1)
    burb_r.append(r)
    burb_atrums.append(randint(1, MAX_BURB_ATR))

# 5. solis
def parvietot_burbulus():
    for i in range(len(burb_id)):               # pārskata katru saraksta burbuļu
        a.move(burb_id[i], -burb_atrums[i], 0)

# 7. solis
def iegut_koord(id_skaitlis):
    poz = a.coords(id_skaitlis)
    x = (poz[0] + poz[2]) / 2
    y = (poz[1] + poz[3]) / 2
    return x, y

# 8. solis
def dzest_burbuli(i):
    del burb_r[i]
    del burb_atrums[i]
    a.delete(burb_id[i])
    del burb_id[i]

# 9. solis
def notirit_burbulus():
    for i in range(len(burb_id)-1, -1, -1):     # pārskata saraksta atpakaļgaitā
        x, y = iegut_koord(burb_id[i])
        if x < -ATSTARPE:
            dzest_burbuli(i)

# 11. solis
def attalums(id1, id2):
    x1, y1 = iegut_koord(id1)
    x2, y2 = iegut_koord(id2)
    return sqrt((x2 - x1)**2 + (y2- y1)**2)

# 12. solis
def sadursme():
    punkti = 0
    for burb in range(len(burb_id)-1, -1, -1):
        if attalums(kuga_id2, burb_id[burb]) < (KUGA_R + burb_r[burb]):
            punkti += (burb_r[burb] + burb_atrums[burb])
            dzest_burbuli(burb)
    return punkti

# 14. solis
a.create_text(50, 30, text="LAIKS", fill="white")
a.create_text(150, 30, text="REZULTĀTS", fill="white")

BURB_NEJAUSI = 10
rezultats = 0
# SPĒLES GALVENAIS CIKLS
while True:
    if randint(1, BURB_NEJAUSI) == 1:
        izveidot_burbuli()
    parvietot_burbulus()
    notirit_burbulus()
    rezultats += sadursme()
    print(rezultats)
    logs.update()   # atjauno logu, lai no jauna uzzīmētu burbuļus
    sleep(0.01)

input()
