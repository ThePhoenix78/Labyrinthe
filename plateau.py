# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module plateau
   ~~~~~~~~~~~~~~

   Ce module gère le plateau de jeu.
"""

from matrice import *
from carte import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """

    inc=0
    matrice=Matrice(7,7)
    lig=getNbLignes(matrice)
    col=getNbColonnes(matrice)
    cartes=creerCartesAmovibles(1,nbTresors)
    for i in range(lig):
        for j in range(col):
            setVal(matrice,i,j,cartes[inc])
            inc+=1

    return matrice,cartes[-1]


def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    liste=[]
    boolean=[False,True]
    i=0
    while i<nbTresors:
        nord=boolean[random.randint(0,1)]
        sud=boolean[random.randint(0,1)]
        est=boolean[random.randint(0,1)]
        ouest=boolean[random.randint(0,1)]
        val=Carte(nord,est,sud,ouest)
        if estValide(val):
            liste.append(val)
            i+=1

    return liste

def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    val=getTresor(plateau[lig][col])
    return val==numTresor

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            val = getTresor(plateau[i][j])
            if val==numTresor:
                return i,j
    return None

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            val = possedePion(plateau[i][j],numJoueur)
            if val:
                return i,j
    return None

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    val=getVal(plateau,lin,col)
    if possedePion(val,numJoueur):
        prendrePion(val,numJoueur)


def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    val=getVal(plateau,lin,col)
    if not possedePion(val,numJoueur):
        poserPion(val,numJoueur)

def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    ligne=getNbLignes(plateau)
    colone=getNbColonnes(plateau)
    suivant=getVal(plateau,ligD,colD)
    arrive=getVal(plateau,ligA,colA)

    lig=ligD
    col=colD

    nord=None
    sud=None
    est=None
    ouest=None

    inc=0

    cheN=0
    cheS=0
    cheE=0
    cheO=0

    prec=""

    while inc<10:

        if lig-1>0 and prec!="sud":
            lig-=1
            val=getVal(plateau,lig,col)
            nord=passageNord(suivant,val)
            if nord:
                print("nord")
                prec="nord"
                suivant=val
                cheN+=1
                if lig==ligA and col==colA:
                    return True
                continue
            else:
                lig+=1

        if lig+1<colone and prec!="nord":
            lig+=1
            val=getVal(plateau,lig,col)
            sud=passageSud(suivant,val)
            if sud:
                print("sud")
                prec="sud"
                suivant=val
                cheS+=1
                if lig==ligA and col==colA:
                    return True
                continue
            else:
                lig-=1

        if col+1<ligne and prec!="ouest":
            col+=1
            val=getVal(plateau,lig,col)
            est=passageEst(suivant,val)
            if est:
                print("est")
                prec="est"
                suivant=val
                cheE+=1
                if lig==ligA and col==colA:
                    return True
                continue
            else:
                col-=1

        if col-1>0 and prec!="est":
            col-=1
            val=getVal(plateau,lig,col)
            ouest=passageOuest(suivant,val)
            if ouest:
                print("ouest")
                test=True
                prec="ouest"
                suivant=val
                cheO+=1
                if lig==ligA and col==colA:
                    return True
                continue
            else:
                col+=1

        if prec=="nord" and cheN>0:
            lig+=1
            cheN-=1
            prec="sud"
            print("sud",1)
        elif prec=="sud" and cheS>0:
            lig-=1
            cheS-=1
            prec="nord"
            print("nord",1)
        elif prec=="est" and cheE>0:
            col-=1
            cheE-=1
            prec="ouest"
            print("ouest",1)
        elif prec=="ouest" and cheO>0:
            col+=1
            cheO-=1
            prec="est"
            print("est",1)
        else:
            prec=""


        inc+=1



    return False

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin,
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    return

if __name__=="__main__":
    plat=Plateau(4,50)
    print(accessible(plat[0],0,0,0,6))
    mat=Matrice(7,7)
    for i in range(len(plat[0])):
        for j in range(len(plat[0])):
            mat[i][j]=listeCartes[coderMurs(plat[0][i][j])]
    for ligne in mat:
        print(ligne)
