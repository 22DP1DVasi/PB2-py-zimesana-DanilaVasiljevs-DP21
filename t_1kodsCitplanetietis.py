# Daņila Vasiļjevs DP2-1

from tkinter import *

# Uzzīmē citplanētieti!

logs = Tk()
logs.title("Citplanētietis")
a = Canvas(logs, height=300, width=400)
a.pack()

kermenis = a.create_oval(100, 150, 300, 250, fill="green")
acs = a.create_oval(170, 70, 230, 130, fill="white")
zilite = a.create_oval(190, 90, 210, 110, fill="black")
mute = a.create_oval(150, 220, 250, 240, fill="red")
kakls = a.create_line(200, 150, 200, 130)
cepure = a.create_polygon(180, 75, 220, 75, 200, 20, fill="blue")

# Objektu izmainīšana
# Figūru pārvietošana

def mute_vala():
    a.itemconfig(mute, fill="black")

def mute_ciet():
    a.itemconfig(mute, fill="red")

# Paslēpšana un parādīšana

def mirkskinat():
    a.itemconfig(acs, fill="green")
    a.itemconfig(zilite, state=HIDDEN)

def nemirkskinat():
    a.itemconfig(acs, fill="white")
    a.itemconfig(zilite, state=NORMAL)

# Runāšana

vardi = a.create_text(200, 280, text="Es esmu citplanētietis!")

def zagt_cepuri():
    a.itemconfig(cepure, state=HIDDEN)
    a.itemconfig(vardi, text="Atdod man cepuri!")

logs.attributes("-topmost", 1)  # novieto Tkinter logu ekrāna priekšplānā

# Reaģēšana uz notikumiem
# Peles notikumi

def zagas(notikums):
    mute_vala()
    a.itemconfig(vardi, text="Ik!")
a.bind_all("<Button-1>", zagas)     # peles kreisās pogas klikšķi piesaista funkcijai zagas

# Taustiņu notikumi

def mirkskinat2(notikums):
    a.itemconfig(acs, fill="green")
    a.itemconfig(zilite, state=HIDDEN)  # paslēpj zīlīti

def nemirkskinat2(notikums):
    a.itemconfig(acs, fill="white")
    a.itemconfig(zilite, state=NORMAL)  # parāda zīlīti

a.bind_all("<KeyPress-a>", mirkskinat2)
a.bind_all("<KeyPress-z>", nemirkskinat2)

# Pārvietošana ar taustiņiem

def acs_vadiba(notikums):
    taustins = notikums.keysym  # nosaka piespiestā taustiņa nosaukumu
    if taustins == "Up":
        a.move(zilite, 0, -1)
    elif taustins == "Down":
        a.move(zilite, 0, 1)
    elif taustins == "Left":
        a.move(zilite, -1, 0)
    elif taustins == "Right":
        a.move(zilite, 1, 0)

a.bind_all("<Key>", acs_vadiba)

#input()
