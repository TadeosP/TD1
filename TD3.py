#EXO 1 et 2

class Tree:
    def __init__(self, label, *children):
        self.__label = label
        self.__children = children

    def __label__(self):
        return str(self.__label)
    
    def __children__(self):
        return self.__children
    
    def nb_children(self):
        return len(self.__children)
    
    def child(self, i : int):
        assert (i<= self.nb_children())
        return self.__children[i-1] # 1 est le numéro du premier sous arbre
    
    def is_leaf(self):
        if self.nb_children()==0:
            return True
        return False
    
    def depth(self): #EXO3
        if self.is_leaf():
            return 0
        else :
            return max((self.child(i)).depth() +1 for i in range(self.nb_children()))
        
    def __str__(self): #EXO4
        resultat = self.__label__() 
        if self.is_leaf():
            return resultat
        else : 
            for i in range(self.nb_children()) :
                if self.nb_children() == 1 :
                    resultat += '(' + self.child(i).__str__() + ')'
                else : 
                    if i == 0 :
                        resultat += '(' + self.child(i).__str__()  
                    if i == self.nb_children() - 1 :
                        resultat += ',' + self.child(i).__str__() + ')'
                    else : 
                        resultat += ',' + self.child(i).__str__() #Renvoie l'arbre avec la dernière branche en double et je n'arrive pas à trouver le problème
        return resultat
    
    def __eq__(self, __value: object) -> bool : #permet de comparer deux arbres
        if self.is_leaf():
            return self.__str__() == __value.__str__()
        else : 
            for i in range(self.nb_children()) :
                return self.__str__() == __value.__str__() and (self.child(i)).__eq__(__value.child(i))
        return True   
    def deriv(self, var: str):  #Exo5 qui n'est pas aboutit
        resultat = ''
        if self.is_leaf():
            if self.__str__() == 'var':
                resultat =  resultat + Tree('1').__str__()
                return resultat
            else:
                return Tree('0')
        else:
            for i in range(self.nb_children()):
                return self.child(i).deriv(var)


G = Tree('f')
T = Tree('f',Tree('a'),Tree('b'))
Tv = Tree('f',Tree('b'),Tree('a'))
Y = Tree('f',Tree('a',Tree('c')),Tree('b',Tree('z',Tree('fg'))), Tree('r'), Tree('tree', Tree('arbre')),Tree('u'))
F = T.child(2)
P = Tree('3*X^2 + 5*X + 7')

assert (F.__label__())=='b'
assert (F.is_leaf())==True
assert (T.nb_children()) == 2
assert Y.__str__() == 'f(u,u,a(c),b(z(fg)),r,tree(arbre))'
assert Y.__eq__(Tv) ==  False
#print (G.deriv('a'))


  


