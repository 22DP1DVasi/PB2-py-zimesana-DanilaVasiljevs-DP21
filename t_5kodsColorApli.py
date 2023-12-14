# Daņila Vasiļjevs DP2-1

from random import *
from tkinter import *

izmers = 500
logs = Tk()
audekls = Canvas(logs, width=izmers, height=izmers)
audekls.pack()
while True:
    krasa = choice(["pink", "orange", "purple", "yellow"])
    x0 = randint(0, izmers)
    y0 = randint(0, izmers)
    d = randint(0, izmers/5)
    audekls.create_oval(x0, y0, x0 + d, y0 + d, fill=krasa)
    logs.update()

