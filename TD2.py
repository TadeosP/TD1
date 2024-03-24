##TD2

##Exo 1


class Fractions:
    def __init__(self,a,b):
        assert b !=0
        self.numerateur = a
        self.denominateur = b
    def __str__(self):
        return f"my value is: {self.numerateur}/{self.denominateur}"

if __name__ == '__main__':
    fr = Fractions(3,4)
    assert fr.__str__() == 'my value is: 3/4'

## Exo 2
from math import gcd   
class Fractions:
    def __init__(self,a,b):
        assert b !=0
        self.numerateur = a 
        self.denominateur = b
    def __str__(self):                               ## Permet d'afficher la fraction
        return f"my value is: {self.numerateur}/{self.denominateur}"
    def __add__(self, other):
        if self.denominateur == other.denominateur :
            a = self.numerateur + other.numerateur
            b = self.denominateur
        else : 
            a = self.numerateur * other.denominateur + other.numerateur * self.denominateur
            b = self.denominateur * other.denominateur
        return Fractions(a,b)
    def __mult__(self,other):
        a= self.numerateur * other.numerateur
        b = self.denominateur * other.denominateur
        return Fractions (a,b)
    def __simplify__(self):
        x=gcd(self.numerateur, self.denominateur)
        a = self.numerateur // x
        b = self.denominateur // x
        return Fractions(a,b)
    
if __name__ == '__main__':
    fr = Fractions(32,40)
    mu = Fractions(1,2)
    a = fr.__mult__(mu)
    b = fr.__simplify__()
    assert a.numerateur == 32
    assert a.denominateur == 80
    assert b.numerateur == 4
    assert b.denominateur == 5

##EXO 3
    
def somme_1_sur_n(n):
    m=Fractions(0,1)
    for i in range(1,n+1):
        m = m.__add__(Fractions(1,i))
    return m.__simplify__()
b=somme_1_sur_n(10000).denominateur
a=somme_1_sur_n(10000).numerateur
assert a/b == 9.787606036044382

##EXO 4

def leibniz(n):
    m=Fractions(0,1)
    for i in range(n):
        m = m.__add__(Fractions((-1)**i,2*i+1))
    return m.__simplify__()
b=leibniz(10000).denominateur
a=leibniz(10000).numerateur
assert a/b == 0.7853731633975108

#Exo 5

 
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients[::-1]  # prend une liste de coefficients dans l'ordre décroissant des puissances de X

    def __str__(self):
        degree=len(self.coefficients)-1
        polynomial_str = ""
        for i, coeff in enumerate(self.coefficients): #utilisée dans la méthode __str__ pour itérer sur les coefficients du polynôme tout en gardant une trace de l'indice
            if coeff != 0:
                if i == 0:
                    term = str(coeff) + " + "
                else:
                    if i != degree:
                        term = f"{coeff}*X^{i} + " 
                    else :
                        term = f"{coeff}*X^{i}" 
                polynomial_str += term
        return polynomial_str

coefficients = [4, 0, 3, 1]  # Coefficients du polynôme [4*X**3 + 3*X + 1]
polynomial = Polynomial(coefficients)
assert polynomial.__str__() == '1 + 3*X^1 + 4*X^3'

## Exo 6

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients[::-1]  # prend une liste de coefficients dans l'ordre décroissant des puissances de X

    def __str__(self):
        degree=len(self.coefficients)-1
        polynomial_str = ""
        for i, coeff in enumerate(self.coefficients): #utilisée dans la méthode __str__ pour itérer sur les coefficients du polynôme tout en gardant une trace de l'indice
            if coeff != 0:
                if i == 0:
                    term = str(coeff)
                else:
                    if i != degree:
                        term = f" + {coeff}*X^{i}" 
                    else :
                        term = f" + {coeff}*X^{i}" 
                polynomial_str += term
        return polynomial_str

    def __add__(self,poly):
        c1=poly.coefficients
        c2=self.coefficients
        l1=min(len(c1),len(c2))
        l2=max(len(c1),len(c2))
        c=[0]*l2
        for k in range (l1):
            c[k]+=(c1[k]+c2[k])
        if len(c1)>len(c2):
            for k in range (l1,l2):
                c[k]+=c1[k]
        else :
            for k in range (l1,l2):
                c[k]+=c2[k]
        return Polynomial(c)

    def __deriv__ (self):
        c = self.coefficients
        for k in range (len(c)):
            c[k] = k * c[k]
        return Polynomial(c)

    def __integrate__(self, constante): # la variable globale constante permet a l'utilisateur de choisir la constante d'intégration
        c1=self.coefficients
        c=[constante]+[0]*len(c1)
        for k in range (1,len(c1)+1):
            c[k]=c1[k-1]/k
        return Polynomial(c)               

X = Polynomial ([1,0,4,5])
Y = Polynomial ([0,2,0,0])
assert X.__str__() =="5 + 4*X^1 + 1*X^3"
assert Y.__str__() == " + 2*X^2"
C = X.__add__(Y)
assert C.__str__() == "1 + 2*X^1 + 4*X^2 + 5*X^3"
C = X.__deriv__()
assert C.__str__() == "3 + 4*X^2"
C = X.__integrate__(0)
assert C.__str__() == "0.75 + 2.0*X^2"