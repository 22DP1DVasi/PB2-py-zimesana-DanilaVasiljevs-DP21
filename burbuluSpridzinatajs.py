# Daņila Vasiļjevs DP2-1

from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt
import pygame

pygame.init()

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

BURBULU_SKANA = pygame.mixer.Sound("411642__inspectorj__pop-high-a-h1.wav")

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
    for i in range(len(burb_id)):         # pārskata katru saraksta burbuļu
        a.move(burb_id[i], -burb_atrums[i], 0)

# 7. solis
def iegut_koord(id_skaitlis):
    poz = a.coords(id_skaitlis)
    x = (poz[0] + poz[2]) / 2
    y = (poz[1] + poz[3]) / 2   # centra koordinātas
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
        if attalums(kuga_id2, burb_id[burb]) < (KUGA_R + burb_r[burb]): # ja attālums no figūru centriem ir mazāks nekā abu rādiusu summa
            punkti += (burb_r[burb] + burb_atrums[burb])
            dzest_burbuli(burb)
            BURBULU_SKANA.play()
    return punkti

# 14. solis
a.create_text(50, 30, text="LAIKS", fill="white")
a.create_text(150, 30, text="REZULTĀTS", fill="white")
laiks_teksts = a.create_text(50, 50, fill="white")
rezultats_teksts = a.create_text(150, 50, fill="white")

def paradit_rezultatu(rezultats):
    a.itemconfig(rezultats_teksts, text=str(rezultats))

def paradit_laiku(laiks_palicis):
    a.itemconfig(laiks_teksts, text=str(laiks_palicis))


# 15. solis
BURB_NEJAUSI = 10
LAIKA_IEROBEZOJUMS = 30
PAPILDLAIKA_REZ = 1000

rezultats = 0
papildu = 0
beigas = time() + LAIKA_IEROBEZOJUMS

# SPĒLES GALVENAIS CIKLS
while time() < beigas:
    if randint(1, BURB_NEJAUSI) == 1:
        izveidot_burbuli()
    parvietot_burbulus()
    notirit_burbulus()
    rezultats += sadursme()
    if (int(rezultats / PAPILDLAIKA_REZ)) > papildu:
        papildu += 1
        beigas += LAIKA_IEROBEZOJUMS
    
    paradit_rezultatu(rezultats)
    paradit_laiku(int(beigas - time()))
    logs.update()   # atjauno logu, lai no jauna uzzīmētu burbuļus
    sleep(0.01)

# 17. solis
a.create_text(VID_X, VID_Y, \
              text="SPĒLES BEIGAS", fill="white", font=("Helvetica", 30))

a.create_text(VID_X, VID_Y + 30, \
              text="Rezultāts: " + str(rezultats), fill="white")

a.create_text(VID_X, VID_Y + 45, \
              text="Papildu laiks: " + str(papildu * LAIKA_IEROBEZOJUMS), fill="white")
pygame.quit()

input()
