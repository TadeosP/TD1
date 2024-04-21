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

def tir(): #EXO2
    scores=0
    for i in range(5):
        x = randint(0, 400)
        y = randint(0, 400)
        scores += score(x,y)
        can.create_oval(max(x-15,0), max(y-15,0), x+15, y+15, outline='grey', fill='black')
    Button(root, text=' score : '+ str(scores) , width=5).grid(row=2,column=1, sticky = E)
    return None

def tir2 ():
    x = randint(0, 400)
    y = randint(0, 400)   
    return can.create_oval(max(x-15,0), max(y-15,0), x+15, y+15, outline='grey', fill='black')

abscisse = can.create_line(0, 200, 400, 200,fill='red')
ordonee = can.create_line(200, 0, 200, 400,fill='red')
can.create_text(50, 50,text='La cible',font=('Times','18','bold'),fill= 'white')
can.grid(row=0,column=0,columnspan=3)
Button(root, text="Feu!", command = tir , width=5).grid(row=2,column=0, sticky = E)
Button(root, text="Quitter", command = root.destroy, width=5).grid(row=2, column=2, sticky= E)  
root.mainloop()

