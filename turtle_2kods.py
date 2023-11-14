# Daņila Vasiļjevs DP2-1

from turtle import *

def brunurupuca_vadiba(dar, vert):
    dar = dar.upper()
    if dar == 'P':
        forward(vert)
    elif dar == 'A':
        backward(vert)
    elif dar == 'L':
        right(vert)
    elif dar == 'K':
        left(vert)
    elif dar == 'N':
        penup()
    elif dar == 'I':
        pendown()
    elif dar == 'J':
        reset()
    else:
        print("Nezināma komanda")


def virknes_tulkotajs(programma):
    kmd_saraksts = programma.split('-')
    for komanda in kmd_saraksts:
        kmd_garums = len(komanda)
        if kmd_garums == 0:
            continue
        kmd_tips = komanda[0]
        sk = 0
        if kmd_garums > 1:
            sk_virkne = komanda[1:]
            sk = int(sk_virkne)
        print(komanda, ':', kmd_tips, sk)
        brunurupuca_vadiba(kmd_tips, sk)


instrukcijas = '''Ievadi programmu bruņurupucim!
Piemēram, P100-L45-N-P100-K45-I-P100-L90-A50.
J = Jauns zīmējums
N/I = Nolikt/Ieslēgt zīmuli
P100 = Uz priekšu 100 soļus
A50 = Atpakaļ 50 soļus
L90 = Pagriezties par 90 grādiem pa labi
K45 = Pagriezties par 45 grādiem pa kreisi'''

ekrans = getscreen()        # saņem datus, kas nepieciešami uznirstošā loga izveidošanai
while True:
    t_programma = ekrans.textinput("Zīmēšanas rīks", instrukcijas)  # nosaka, ko parādīt uznirstošajā logā
    print(t_programma)
    if t_programma == None or t_programma.upper() == "BEIGT":   # aptur programmu, ja lietotājs uzraksta "BEIGT" vai klikšķina uz pogas "Cancel"
        break
    virknes_tulkotajs(t_programma)
