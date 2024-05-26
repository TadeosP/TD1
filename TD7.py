import numpy as np
import random
from tkinter import Tk, ttk, Canvas, Button, TOP, LEFT, RIGHT, ALL
from tkinter import *
root = Tk()
can = Canvas(root, width=500,height=500,bg='white')
can.grid(row=0,column=0)
col_index = [0,3,1,2,16,5,9,24,11,4,23,14]

COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']
 
graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]

pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])

def draw(can, graph, pos, col_index): #EXO1
    N = len(graph)
    for e in can.find_all():
        can.delete(e)
    for i in range(N):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for i in range(N):
        x, y = pos[i]
        can.create_oval(x-6, y-6, x+6, y+6, fill=COLORS[col_index[i]])
        can.create_text(x-12,y,text=f"{i}")
draw(can,graph,pos, col_index) #EXO1 présentation du graphe


#EXO2


def min_local(i, graph, color):
    minlocal = color[i]
    for j in range(len(graph)) :
        if i in graph[j]:
            if color[j] < minlocal :
                minlocal = color[j]
    for e in graph[i]:
        if color[e] < minlocal :
            minlocal = color[e]
    for j in range(len(graph)) :
        if i in graph[j]:
            color[j] = minlocal
    for e in graph[i]:
        color[e]=minlocal
    return color

def coloriage(graph, color):
    for i in range(len(graph)):
        color = min_local(i,graph,color)
    return color

graphe = [[2], [], [4], [1], [6], [3], [7], [5]]

color =[1,7,9,12,0,3,23,21]
colorie = coloriage(graphe,color)
pose = [[100, 200], [450, 200], [150, 200], [400, 200], [200, 200], [350, 200], [250, 200], [300, 200]]


#draw(can,graphe,pos, colorie) #EXO2 avec le graphe conseillé dans l'exo 2
draw(can,graph,pos, coloriage(graph,col_index)) # avec le graphe de l'énoncé, pour l'exo 3 on reconnait les composantes connexe à leur couleur commune


#EXO4

def color_generator():
    r, g, b = random.randint(0,255), random.randint(0,255),random.randint(0,255)
    return f"#{r:02x}{g:02x}{b:02x}"


def cafew_generator(n): # n est la taille du canva ici n=500
    d=dict()
    color_index = dict()
    color_index[(0,0)] = color_generator()
    i,j=0,0
    while i <n and j<n:
        if random.random()<0.40:
            d[(i,j)]=[(i+1,j)]
            color_index[(i+1,j)] = color_generator()
        if random.random()<0.40:
            if (i,j) not in d:
                d[(i,j)]= [(i,j+1)]
                color_index[(i,j+1)]= color_generator()
            else:
                d[(i,j)].append((i,j+1))
        
        i,j= i+1 ,j + 1 #Ne prends pas en compte tous les points du cadrillage
    return d, color_index                               
graphee, cole_index = cafew_generator(500)

def draw2(can, graph, col_index): 
    N = len(graph)
    for e in can.find_all():
        can.delete(e)
    for cle,valeur in graph.items():
        (a,b)=valeur[0]
        can.create_line(cle[0],cle[1],a,b)
    #for i in range(N):
        #for j in range (N):
            #can.create_oval(i-6, j-6, i+6, j+6, fill=COLORS[col_index[(i,j)]]) #Problème :  Couleur sous format str pas autorisé, c'est bizarre

#draw2(can,graphee, cole_index) #EXO4 Ne fonctionne pas encore
root.mainloop()