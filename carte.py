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
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    DictCarte={"tresor":tresor,"ListePions":pions,"nord":nord,"est":est,"sud":sud,"ouest":ouest}
  

    return DictCarte

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    Valide=True
    NbCarte=0
    if DictCarte["nord"]==True:
      NbCarte=NbCarte+1
    if DictCarte["est"]==True:
      NbCarte=NbCarte+1
    if DictCarte["sud"]==True:
      NbCarte=NbCarte+1
    if DictCarte["ouest"]==True:
      NbCarte=NbCarte+1

    if NbCarte > 2 :
      Valide==False
    
    
    return Valide

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    PresenceMur=True
    if DictCarte["nord"]==False:
      PresenceMur=False
      

    return PresenceMur

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    PresenceMur=True
    if DictCarte["sud"]==False:
      PresenceMur=False

    return PresenceMur

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    PresenceMur=True
    if DictCarte["est"]==False:
      PresenceMur=False

    return PresenceMur

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    PresenceMur=True
    if DictCarte["ouest"]==False:
      PresenceMur=False

    return PresenceMur

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    
    return DictCarte["ListePions"]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    DictCarte["ListePions"]=listePions



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
    ExistePion=True
    if pion not in DictCarte["ListePions"]:
      ExistePion=False

    return ExistePion


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """

    return DictCarte["tresor"]
    

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    tresor=DictCarte["tresor"]
    DictCarte.pop("tresor")
    
    return tresor


def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    TresorsSurCarte=DictCarte[c]
    TresorAncien=PionsSurCarte[0]
    TresorsSurCarte.insert(0,tresor)


    return TresorAncien


def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """


    pass


def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    pass


def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    pass


def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    pass


def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    pass


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
    pass


def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    pass


def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    pass


def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass


def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass


def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass


def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass



if __name__=="__main__":

