# -*- coding: utf-8 -*-
"""
        Projet Labyrinthe
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module carte
   ~~~~~~~~~~~~

   Ce module gère les cartes du labyrinthe.
"""
import random

#Dominique
#Lecocq

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes = ['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    return {"nord":nord,"est":est,"sud":sud,"ouest":ouest,"ListePions":pions.copy(),"tresor":tresor}

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    Valide=False
    NbCarte=0
    for x, y in c.items():
        if y==True:
            NbCarte=NbCarte+1

    if NbCarte<3:
      Valide=True

    return Valide

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c["nord"]

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c["sud"]

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c["est"]

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c["ouest"]

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["ListePions"]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["ListePions"]=listePions


def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(getListePions(c))

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    return pion in c["ListePions"]


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["tresor"]


def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    tresor=c["tresor"]
    c["tresor"]=0
    return tresor


def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    TresorAncien=c["tresor"]
    c["tresor"] = tresor

    return TresorAncien


def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion in c["ListePions"]:
        if len(c["ListePions"])==1:
            c["ListePions"]=[]
        else:
            c["ListePions"].remove(pion)


def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c["ListePions"]:
      c["ListePions"].append(pion)


def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    VariableNord=c["nord"]
    c["nord"]=c["ouest"]
    c["ouest"]=c["sud"]
    c["sud"]=c["est"]
    c["est"]=VariableNord


def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    VariableOuest=c["ouest"]
    c["ouest"]=c["nord"]
    c["nord"]=c["est"]
    c["est"]=c["sud"]
    c["sud"]=VariableOuest


def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    alea=random.randint(0,3)
    for i in range(alea):
        tournerHoraire(c)


def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire
    est de la forme bNbEbSbO où bN, bE, bS et bO valent
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    val=""
    if murOuest(c):
        val+="1"
    else:
        val+="0"
    if murSud(c):
        val+="1"
    else:
        val+="0"
    if murEst(c):
        val+="1"
    else:
        val+="0"
    if murNord(c):
        val+="1"
    else:
        val+="0"

    return int(val,2)


def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    code=bin(code).replace("0b","")
    code="0"*(4-len(code))+code

    c["ouest"]= bool(int(code[0]))
    c["sud"]= bool(int(code[1]))
    c["est"]= bool(int(code[2]))
    c["nord"]= bool(int(code[3]))


def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    return listeCartes[coderMurs(c)]


def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """

    return not (murNord(carte1) or murSud(carte2))


def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return not (murSud(carte1) or murNord(carte2))


def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return not (murOuest(carte1) or murEst(carte2))


def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """

    return not (murEst(carte1) or murOuest(carte2))


if __name__=="__main__":
    carte=Carte( True, True, False, False, 1, pions=[1,2,3])
    carte2=Carte( False, True, False, True, 2, pions=[1,2,9])
    print(possedePion(carte,9))
    print("-------")
    print(passageEst(carte,carte2))
    print(passageOuest(carte,carte2))
    print(passageNord(carte,carte2))
    print(passageSud(carte,carte2))
    print("-------")
    print(carte)
    a=prendreTresor(carte)
    print(carte,a)
    mettreTresor(carte,5)
    tournerHoraire(carte)
    print(carte)
    b=toChar(carte)
    print(b)
    z=coderMurs(carte)
    print(z)
    decoderMurs(carte,z)
