#EXO1

class PolynomialZ:
    def __init__(self, coefficients, n , q): #L'utilisateur envoies un polynome dans le bon ensemble
        self.__n = n 
        self.__q = q
        self.__coefficients = coefficients[::-1] # prend une liste de coefficients dans l'ordre décroissant des puissances de X
        assert len(self.__coefficients) <= self.__n #Vérification de l'entrée de l'utilisateur
        assert max(self.__coefficients) < self.__q

    def __str__(self):
        degree=len(self.__coefficients)-1
        polynomial_str = ""
        for i, coeff in enumerate(self.__coefficients): #utilisée dans la méthode __str__ pour itérer sur les coefficients du polynôme tout en gardant une trace de l'indice
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

    def __add__(self,poly): #EXO2
        assert self.__n == poly.__n
        assert self.__q == poly.__q
        c1 = poly.__coefficients
        c2 = self.__coefficients
        l1 = min(len(c1),len(c2))
        l2 = max(len(c1),len(c2))
        c=[0]*l2
        for k in range (l1):
            c[k]+=(c1[k]+c2[k]) % self.__q #Le coefficient sommé doit respecter les règles d'encodage
        if len(c1)>len(c2):
            for k in range (l1,l2):
                c[k]+=c1[k]
        else :
            for k in range (l1,l2):
                c[k]+=c2[k]
        return PolynomialZ(c,self.__n, self.__q)
    
    def __mul__(self, poly): #EXO3
        assert self.__n == poly.__n
        assert self.__q == poly.__q
        c1 = self.__coefficients
        c2 = poly.__coefficients
        c=[0]*self.__n
        for i in range (len(c1)):
            for j in range (len(c2)):
                a = (i+j)% self.__n
                c[a] += (c1[i]* c2[j])
        for i in range (self.__n):
            c[i] = c[i] % self.__q
        return PolynomialZ(c,self.__n, self.__q)

    def rescale(self, r): #EXO 4 mal fait
        c = self.__coefficients
        c = c % r
        return PolynomialZ(c, self.__n, r)
    
    def scalar(self, c): #EXO4
        l = self.__coefficients
        for i in range(len(l)):
            l[i] = (l[i]* c) % self.__q
        return PolynomialZ(l, self.__n, self.__q)

X = PolynomialZ ([1,0,4,5],4,7)
Y = PolynomialZ ([2,0,3,5],4,7)
V = PolynomialZ ([1,0,4,2],4,5)
Z = PolynomialZ ([1,2,3],4,5)
assert X.__str__() == "5 + 4*X^1 + 1*X^3" #EX01
assert (X + Y).__str__() == "3 + 3*X^3" #EXO2
assert (V.__mul__(Z)).__str__() == "2 + 2*X^2 + 3*X^3" #EXO3
assert (X.scalar(3)).__str__() == "3 + 5*X^2 + 1*X^3" #EXO4 scalar