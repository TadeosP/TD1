from tkinter import Tk, ttk, Canvas, Button, TOP, LEFT, RIGHT, ALL
from tkinter import *
from random import randint
from math import sqrt

def cercle(x,y,r,couleur=''):
    return can.create_oval(x-r, y-r, x+r, y+r, outline='red', fill=couleur)

root = Tk()
r = 180
n = 1
can = Canvas(root, width=400,height=400,bg='red')
can.pack()
while r !=0:
    if r == 60 : 
        cercle(200,200,r,couleur='red')
        can.create_text(200, 200 - r + 15 ,text= str(n),font=('Times','18','bold'),fill= 'ivory')
        n += 1
        r = r - 30
    else :
        cercle(200,200,r,couleur='ivory')
        can.create_text(200, 200 - r + 15,text=str(n),font=('Times','18','bold'),fill= 'red')
        r = r - 30
        n += 1

def score (x,y):
    r=180
    m=0
    while sqrt((x-200)**2 + (y-200)**2) <r :
        r = r - 30
        m += 1
    return m 
n=5 #Nombre de balles initialement présentes qui va s'actualister avec tir2 au nombre de balles restantes après avoir fait f-tirs
scores=0 #Score initial qui s'actualise car variable globale

def tir(): #EXO2  Meilleure score 18 : Bon courage pour faire mieux #J'aidelachance
    global n
    global scores
    for i in range(n):
        x = randint(0, 400)
        y = randint(0, 400)
        scores += score(x,y)
        can.create_oval(x-15, y-15, x+15, y+15, outline='grey', fill='black')
        n-=1
    Button(root, text=' score : '+ str(scores) , width=5).grid(row=2,column=1, sticky = E)
    feu.config(state="disabled") #Permet de tirer seulement une rafale de 5 tirs
    return n, scores

def tir2 (e): #EXO3
    global n
    global scores
    if n==0 :
        root.unbind("<KeyPress-f>") #Pour desactiver la liason entre la touche f et le fonction tir2
    else :
        x = randint(0, 400)
        y = randint(0, 400)
        scores += score(x,y)
        n-=1
        can.create_oval(x-15, y-15, x+15, y+15, outline='grey', fill='black')
        Button(root, text=' score : '+ str(scores) , width=5).grid(row=2,column=1, sticky = E)
    return n, scores

abscisse = can.create_line(0, 200, 400, 200,fill='red')
ordonee = can.create_line(200, 0, 200, 400,fill='red')
can.create_text(50, 50,text='La cible',font=('Times','18','bold'),fill= 'white')
can.grid(row=0,column=0,columnspan=3)
feu = Button(root, text="Feu!", command = tir, width=5) #EXO2
feu.grid(row=2,column=0, sticky = E)
tirf = root.bind("<f>",tir2) #EXO3
Button(root, text="Quitter", command = root.destroy, width=5).grid(row=2, column=2, sticky= E)  


####

Button(root,text="Clic sur <a> pour un jeu de précision").grid(row=2,column=1) #EXO4 

mireobject1 = can.create_oval(200-15, 200-15, 200+15, 200+15, outline='black', fill='systemTransparent') # Création de la mire
mireobject2 = can.create_oval(200-3, 200-3, 200+3, 200+3, outline='black', fill='black')
mireobject3 = can.create_line(185, 200, 215, 200,fill='black')
mireobject4 = can.create_line(200, 185, 200, 215,fill='black')

def mire(event): 
    global mireobject1
    global mireobject2
    global mireobject3
    global mireobject4
    dx = randint(-50, 50)
    dy = randint(-50, 50)
    can.move(mireobject1, dx, dy)
    can.move(mireobject2, dx, dy)
    can.move(mireobject3, dx, dy)
    can.move(mireobject4, dx, dy)
    root.unbind("<KeyPress-f>") #Permet d'arrêter le premier jeu
    feu.config(state="disabled") #idem
    root.bind("<f>", tir3)  #Permet de commencer le deuxième jeu
    root.unbind("<KeyPress-a>")
    root.after(200, mire2)

i =0 # compteur pour arrêter le déplacement de la mire après le tire

def mire2 ():
    global i
    global mireobject1
    global mireobject2
    global mireobject3
    global mireobject4
    if i == 1 :
        root.after_cancel()
    else :
        dx = randint(-50, 50)
        dy = randint(-50, 50)
        can.move(mireobject1, dx, dy)
        can.move(mireobject2, dx, dy)
        can.move(mireobject3, dx, dy)
        can.move(mireobject4, dx, dy)
        root.after(200, mire2)

def tir3(e):
    global i #permet d'arreter la mire après le tire
    global scores
    global mireobject1
    global mireobject2
    global mireobject3
    global mireobject4
    i +=1
    x = can.coords(mireobject1)[0] + 15
    y = can.coords(mireobject1)[1] + 15
    scores += score(x,y)
    can.create_oval(x-15, y-15, x+15, y+15, outline='grey', fill='black')
    Button(root, text=' score : '+ str(scores) , width=5).grid(row=2,column=1, sticky = E)
    root.unbind("<KeyPress-f>")  #Permet de ne pouvoir tirer qu'une seule fois

    

root.bind("<a>",mire)

root.focus_set()
root.mainloop()