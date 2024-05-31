#EXO 1

import struct

f = open("the_wall.wav", "rb")
data = f.read()
#print(len(data))
#print(data[40:45]) 
assert len(data) == 10786340 #Taille totale du fichier
assert len(data[44:]) == 10786296 #Taille du fichier en enlevant l'entète
assert data[22:24] == b'\x02\x00' # 2 channels 

def read_u4(data, pos):
    res = 0
    for i in range(4):
        res =res*256 + data[pos+3-i]
    return res

assert (read_u4(data, 4),) == struct.unpack_from("I",data,4) # équivalence entre les deux méthodes

def creation_de_liste_voies(data):
    C1,C2 =[],[]
    for i in range(44,len(data),4):
        C1.append(struct.unpack_from('H', data, i)[0])
        C2.append(struct.unpack_from('H', data, i+2)[0])
    return C1,C2
C1,C2 = creation_de_liste_voies(data)

def nombre_echantillon(data):
    C1,C2 = creation_de_liste_voies(data)
    return len(C1),len(C2) #Renvoies le nombres d'échantillon dans chaque voie


assert nombre_echantillon(data) == (2696574, 2696574) # il y a 2696574 échantillons par voie


def creation_de_liste_voies2(filename = str): # Version de l'exo 1 avec le nom du fichier en entrée
    f = open(filename, "rb")
    data = f.read() 
    C1,C2 =[],[]
    for i in range(44,len(data),4):
        C1.append(struct.unpack_from('H', data, i)[0])
        C2.append(struct.unpack_from('H', data, i+2)[0])
    return C1,C2


def nombre_echantillon2(filename):     
    C1,C2 = creation_de_liste_voies2(filename)
    return len(C1),len(C2)


assert nombre_echantillon2("the_wall.wav") == (2696574, 2696574) # il y a 2696574 échantillons par voie

##EXO 2

def getheader(filename = str):
    f = open(filename, "rb")
    get = f.read(44)
    return get


def creation(newfilename = str, oldfilename = str): # Copie du fichier wave de base
    header = getheader(oldfilename)
    C1,C2 = creation_de_liste_voies2(oldfilename)
    with open(newfilename,"wb") as f:
        f.write(header)
        for i in range(len(C1)):
            s = struct.pack("HH",C1[i],C2[i])
            f.write(s)
    return f

#creation(filename, "the_wall.wav") Pour tester l'algorithme du dessus en remplacant "filename" par un fichier wav vierge

def creation2(filename, header, C1, C2): # Même script qu'au dessus en connaissant seulement le header ainsi que C1 et C2
    with open(filename,"wb") as f:
        f.write(header)
        for i in range(len(C1)):
            s = struct.pack("HH",C1[i],C2[i])
            f.write(s)
    return f

header = getheader("the_wall.wav")
C1,C2 = creation_de_liste_voies2("the_wall.wav")
#creation2(filename, header, C1, C2) Permet de lancer la creation du fichier wav si un fichier est créé auparavant qui remplace "filename"

#EXO 3

def creation3(filename, header, C1, C2): # Même script qu'au dessus en connaissant seulement le header ainsi que C1 et C2
    with open(filename,"wb") as f:
        f.write(header)
        for i in range(0,len(C1),2): #pas de 2 pour enlever un échantillon sur deux 
            s = struct.pack("HH",C1[i],C2[i])
            f.write(s)
    return f

header = getheader("the_wall.wav")
C1,C2 = creation_de_liste_voies2("the_wall.wav")

#creation3(filename, header, C1, C2) Permet de lancer la creation du fichier wav si un fichier est créé auparavant qui remplace "filename"
## On remarque le l'audio est acceléré par 2!

#EXO 4

def interpole(oldfilename,newfilename):

    C1,C2 = creation_de_liste_voies2(oldfilename)
    A1 = []
    A2 = []
    for i in range(0,len(C1)-1):
        A1.append(C1[i])
        A2.append(C2[i])
        A1.append((C1[i]+C1[i+1])/2)
        A2.append((C2[i]+C2[i+1])/2)
    A1.append(C1[-1])
    A2.append(C2[-1])
    header = getheader(oldfilename)[:40]
    header += struct.pack("I",(len(A1)*2-1)*4)
    header = header[:4] + struct.pack("I",(len(A1)*2-1)*2*4+44) + header[8:]
    with open(newfilename,"wb") as f:
        f.write(header)
        for i in range(len(A1)):
            s = struct.pack("HH", int(A1[i]) , int(A2[i]))
            f.write(s)
    return f
#interpole("the_wall.wav", "audioexo4.wav") L'audio est ralentie par deux et est de très mauvaise qualitée
# Le script interpole permet de ralentir l'audio par 2
