#EXO 1 et 2

import matplotlib.pyplot as plt

h = lambda s : sum([ord(c) for c in s]) # h une fonction de hachage “naïve” sur les chaînes qui somme des codes ascii des caractères
assert h('abc') == 294

class Hashtable :
    def __init__(self,h,N):
        self.__hachingfunction = h
        self.__len = N
        self.__tableau = [None]*N

    def __put__(self, key, value) :
        i = (self.__hachingfunction(key)) % (self.__len)
        if self.__tableau[i] == None :
            self.__tableau[i] = [[key,value]]
        else :
            for j in  range(len(self.__tableau[i])):
                if self.__tableau[i][j][0] == key :
                    self.__tableau[i][j][1] = value
                else :
                    self.__tableau[i].append([key,value])
        return self.__tableau
    
    def __get__(self,key): #EXO3
        i = (self.__hachingfunction(key)) % (self.__len)
        if self.__tableau[i] == None :
            return None
        else :
            for j in range(len(self.__tableau[i])):
                if self.__tableau[i][j][0] == key :
                    return self.__tableau[i][j][1]
        return None
    
    def repartition(self): #EXO4
        N=self.__len
        t=[0] * N
        for i in range(N):
            if self.__tableau[i] != None :
                t[i] = len(self.__tableau[i])
        return t
    def resize(self): #EXO6
        m=0
        N= self.__len
        for j in  range(len(self.__tableau)):
            for i in  range(len(self.__tableau[j])):
                if self.__tableau [j][i] != None :
                    m+=1
        if m >= 1.2 * N :
            return self.__tableau + [None]*N
        return self.__tableau
        

ht = Hashtable(h, 10) #EXO 4
ht.__put__('aaa',7)
ht.__put__('bac',4)
ht.__put__('abc',4)
ht.__put__('baa',5) # connaissant h, on sait que 'baa','aba' et 'aab' vont être en collision
ht.__put__('aba',4)
ht.__put__('aab',3)
ht.__put__('a',6)


assert ht.__get__('abc') == 4
assert ht.__get__('aaa') == 7
assert ht.__put__('a',6) == [None, [['aaa', 7]], [['baa', 5], ['aba', 4], ['aab', 3], ['aab', 3]], None, [['bac', 4], ['abc', 4]], None, None, [['a', 6]], None, None]

Ht = Hashtable (h, 10000) #EX0 5

f = open('frenchssaccent.dic','r') #utilisation de lexique frenchssaccent.dic
t=[]
for ligne in f:
    t.append(ligne[0:len(ligne)-1])
f.close()

for i in range(len(t)):
    Ht.__put__(t[i],len(t[i]))


y = Ht.repartition() #EXO5
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")
plt.show()
