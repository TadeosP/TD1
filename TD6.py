graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

#EXO1
import numpy as np
import random
from tkinter import Tk, ttk, Canvas, Button, TOP, LEFT, RIGHT, ALL
from tkinter import *
from math import sqrt
root = Tk()
can = Canvas(root, width=400,height=400,bg='white')
can.grid(row=0,column=0)

pos = np.array([(400 * random.random(), 400 * random.random())
       for i in range(len(graph))])
# Pour le calcul de la force on suppose avoir le même ressort pour chaque arete donc k elle le même partout
lo=100
k=50
def force(l,u):
    return (k*(l-lo))*u
def norme(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
#def unitaire(a,b):

#vit = np.array([((random.random()-0.5)*10, (random.random()-0.5)*10) #Exo2
       #for i in range(len(graph))])


def draw(can, graph, pos):
    for i in range(len(graph)):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")
draw(can,graph,pos)
root.mainloop()

# pas terminé car présent qu'une heure en TD

