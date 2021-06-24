from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter.constants import DISABLED, NORMAL
import sys
import random

IKKUNAN_LEVEYS = 500
IKKUNAN_KORKEUS = 250

def aloita():
    vastausikkuna['text'] = "Tervetuloa numeroiden Master Mindiin"
    r = satunnaisrivi()
    #print ("Ohjelma arpoi rivin "+r)
    vastausikkuna['text'] = "Peli alkaa"
    rivi_ikkuna['text'] = r
    numeroikkuna['text'] = "1"
    tarkista_button['state'] = NORMAL
    aloita_button['state'] = DISABLED

def pelaa():
    arv_no = int(numeroikkuna.cget("text"))
    arvausrivi = Entry.get(arvauskentta)
    oikea = False
    if len(arvausrivi)!=4:
            arvauskentta.delete(0,'end')
            vastausikkuna['text'] = "Syötä neljä merkkiä"
    elif not oikeat_merkit(arvausrivi):
            arvauskentta.delete(0,'end')
            vastausikkuna['text'] = "Merkkien pitää olla välillä 1-6"
    else:
        oikea = True
    if oikea:
        rivi = rivi_ikkuna.cget("text")
        if arvausrivi == rivi:
            vastausikkuna['text'] = "Onnittelut! Arvasit rivin."
            uusi_peli()
        else:
            oikea_paikka, vaara_paikka = tarkasta_numerot(rivi,arvausrivi)
            arvauskentta.delete(0,'end')
            vastausikkuna['text'] = "Oikeilla / väärillä paikoilla: "+str(oikea_paikka)+"/"+str(vaara_paikka)
            print(arv_no)
            print(arvausrivi)
            print(oikea_paikka,"/",vaara_paikka)
            if arv_no < 10:
                arv_no += 1
                numeroikkuna['text'] = str(arv_no)
            else:
                vastausikkuna['text'] = "Oikea rivi on"+rivi
                numeroikkuna['text'] = "1"
                uusi_peli()
                
def uusi_peli():
    aloita_button['state'] = NORMAL
    tarkista_button['state'] = DISABLED
    arvauskentta.delete(0,'end')

def satunnaisrivi():
    r = ""
    for x in range(1,5):
        luku = random.randrange(1,6)
        r += str(luku)
    return r


def oikeat_merkit(syote):
    om = True
    for x in range(0,4):
        if (syote[x])not in ['1','2','3','4','5','6']:
            om = False
    return om

def tarkasta_numerot(r,ar):
    r = list(r)
    ar = list(ar)
    op = 0
    vp = 0
    for x in range(0,4): #oikea numero oikealla paikalla
        if ar[x]==r[x]:
            op += 1
            ar[x]=str(7) #sijainnista vertaaminen ei enää onnistu
            r[x]=str(0) #tästä ei voi enää löytää samalla numerolla
    if op < 3: #jos oikeilla paikoilla 3, neljännen täytyy olla väärä kirjain
        for x in range(0,4): #oikea numero väärälla paikalla
            for y in range(0,4):
                if ar[x]==r[y] and x!=y:
                    vp += 1
                    ar[x]=str(7) #sijainnista vertaaminen ei enää onnistu
                    r[y]=str(0) #tästä ei voi enää löytää samalla numerolla
    return op,vp

def lopeta():
    ikkuna.destroy() #Suljetaan ikkuna
    sys.exit(0)

ikkuna = Tk()
ikkuna.title("MASTER MIND: NUMEROT")

ikkuna.geometry(str(IKKUNAN_LEVEYS) + "x" + str(IKKUNAN_KORKEUS))

ruutu1 = Frame(ikkuna, borderwidth = 3)
ruutu1.pack()

ruutu2 = Frame(ruutu1, borderwidth = 3)
ruutu2.pack(side = RIGHT)

arvauskentta = Entry(ruutu1) #Käyttäjä kirjoittaa arvauksensa
arvauskentta.pack()
arvauskentta.focus_set()

nrotietoikkuna = Label(ruutu1,text = "Arvauksesi numero") 
nrotietoikkuna.pack()

numeroikkuna = Label(ruutu1,text = "1") #Ilmoittaa, kuinka mones arvaus
numeroikkuna.pack()

vastausikkuna = Label(ruutu1,text = "Tervetuloa numerojen Master Mindiin") #Ilmoitetaan tulos
vastausikkuna.pack()

rivi_ikkuna = Label(ruutu1,text = "") #Arvottu rivi merkitään muistiin
rivi_ikkuna.pack_forget()

aloita_button = Button(ruutu2, text = "Aloita peli", \
                       width = 12, command = aloita)
aloita_button.pack(side = TOP)

tarkista_button = Button(ruutu2, text = "Tarkista vastaus", \
                       width = 12, command = pelaa, state= DISABLED)
tarkista_button.pack(side = TOP)

lopeta_button = Button(ruutu2, text = "Lopeta", \
                       width = 12, command = lopeta)
lopeta_button.pack(side = BOTTOM)

ikkuna.mainloop() #Ohjelman käynnistys

