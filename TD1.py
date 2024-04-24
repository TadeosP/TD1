##EXO 1 et 2

f = open('frenchssaccent.dic','r')
t=[]
for ligne in f:
    t.append(ligne[0:len(ligne)-1])
f.close()

tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j','z','l']

def doublon(l):     ## Renvoie True lorsqu'il y a des doublons dans un liste
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j] :
                return True
    return False

def long(l):       ##Renvoie le mot le plus long d'une liste
    m=len(l[0])
    n=l[0]
    for i in range(len(l)):
        if len(l[i])>m:
            m=len(l[i])
            n=l[i]
    return n

def scrable(tirage,t): #Renvoie le mot le plus long que l'on peut faire avec le tirage
    s=[]
    mots_possibles=[]
    i=0
    for elt in t:
        s.append(list(elt))
        if set(s[i]).intersection(tirage)==set(s[i]) and doublon(s[i])==False:
            mots_possibles.append(elt)
        i+=1
    return (mots_possibles , long(mots_possibles))

assert scrable(tirage,t) == (['a', 'aber', 'able', 'ace', 'acre', 'age', 'al', 'ale', 'arc', 'are', 'arec', 'ars', 'as', 'bac', 'bal', 'bar', 'barge', 'bas', 'base', 'baser', 'bec', 'bel', 'ber', 'blase', 'blaser', 'blazer', 'br', 'bras', 'brase', 'cab', 'cabre', 'cage', 'cal', 'cale', 'caler', 'car', 'cas', 'case', 'caser', 'ce', 'cg', 'cl', 'clebs', 'cr', 'crabe', 'crase', 'czar', 'erg', 'ers', 'es', 'gal', 'galbe', 'galber', 'gale', 'garce', 'gare', 'gars', 'gaz', 'gaze', 'gazer', 'gel', 'glabre', 'glace', 'glacer', 'glas', 'grec', 'jable', 'jabler', 'jale', 'jar', 'jars', 'jas', 'jase', 'jaser', 'je', 'la', 'labre', 'lac', 'lace', 'lacer', 'lare', 'large', 'las', 'laser', 'lb', 'le', 'legs', 'les', 'lez', 'ra', 'race', 'racle', 'rage', 'rase', 'raz', 'reg', 'rel', 'sa', 'sable', 'sabler', 'sabre', 'sac', 'sacre', 'sage', 'sale', 'saler', 'sarcle', 'scare', 'se', 'sel', 'zabre'], 'blaser')

##camille.lanuel@loria.fr lui envoyer le lien du dépot https

###EXO 3
##Il faut utiliser des dictionnaires pour attribuer des valeurs aux lettres

dico={}
dico={x:1 for x in ['a','e','i','l','n','o','r','s','t','u']}
for x in ('d','g','m'):
    dico[x]=2
for z in ['b','c','p']:
    dico[z]=3
for z in ['f','h','v']:
    dico[z]=4
for z in ['k','w','x','y','z']:
    dico[z]=10
dico['j']=8
dico['q']=8

##points_alphabet = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,'K': 10, 'L': 1, 'M': 2, 'N': 1, 'O': 1,'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1,'U': 1, 'V': 4, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}

def score(mot):
    m=0
    l=list(mot)
    for x in l:
        m+=dico[x]
    return m
assert score('a') == 1
assert score('lettre') == 6
assert score('scrabble') == 14

##une fonction max_score qui prend une liste de mots et retourne le mot correspondant au plus grand nombre de points, ainsi que le nombre de points
def max_score(l):
    m=score(l[0])
    n='l[0]'
    for x in l:
        if score(x)>m:
            m=score(x)
            n= x
    return (n,m)
assert max_score(['rte', 'ver', 'ce', 'etc', 'cet', 'ex', 'cr', 'et', 'ter', 'te', 'ct']) == ('ex', 11)

(mots_possibles,long)=scrable(tirage,t)
mots_avec_max_points = max_score(mots_possibles)
assert mots_avec_max_points ==('blazer', 17)
