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
    matrice=Matrice(7,7)
    lig=getNbLignes(matrice)
    col=getNbColonnes(matrice)

    cartes=creerCartesAmovibles(1,nbTresors)
    
    for i in range(lig):
        for j in range(col):
            if i==j==0:
                setVal(matrice,i,j,Carte(True,False,False,True))
            elif i==0 and j==col-1:
                setVal(matrice,i,j,Carte(True,True,False,False))
            elif i==lig-1 and j==0:
                setVal(matrice,i,j,Carte(False,False,True,True))
            elif i==lig-1 and j==col-1:
                setVal(matrice,i,j,Carte(False,True,True,False))

            elif i==0 and j%2==0:
                setVal(matrice,i,j,Carte(True,False,False,False))
            elif i==lig-1 and j%2==0:
                setVal(matrice,i,j,Carte(False,False,True,False))

            elif i%2==0 and j==0:
                setVal(matrice,i,j,Carte(False,False,False,True))
            elif i%2==0 and j==col-1:
                setVal(matrice,i,j,Carte(False,True,False,False))

            else:
                setVal(matrice,i,j,cartes.pop(0))

    return matrice,cartes.pop()


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

    for i in range(16):
        carte=Carte(True,True,False,False)
        tourneAleatoire(carte)
        liste.append(carte)

    for i in range(12):
        carte=Carte(True,False,True,False)
        tourneAleatoire(carte)
        liste.append(carte)

    for i in range(10):
        carte=Carte(True,False,False,False)
        tourneAleatoire(carte)
        liste.append(carte)

    random.shuffle(liste)

    mettreTresor(liste[0],tresorDebut)

    for i in range(tresorDebut,nbTresors):
        mettreTresor(liste[i],i)


    random.shuffle(liste)

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
    if val==numTresor:
        prendreTresor(plateau[lig][col])
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

    matrice=Matrice(ligne,colone)

    setVal(matrice,ligD,colD,1)

    for i in range(ligne*colone):
        for lig in range(ligne):
            for col in range(colone):
                if getVal(matrice,lig,col)==1:

                    case=getVal(plateau,lig,col)
                    setVal(matrice,lig,col,2)

                    if lig-1>0:
                        val=getVal(plateau,lig-1,col)
                        if passageNord(case,val) and getVal(matrice,lig-1,col)!=2:
                            setVal(matrice,lig-1,col,1)

                    if lig+1<colone:
                        val=getVal(plateau,lig+1,col)
                        if passageSud(case,val) and getVal(matrice,lig+1,col)!=2:
                            setVal(matrice,lig+1,col,1)

                    if col+1<ligne:
                        val=getVal(plateau,lig,col+1)
                        if passageEst(case,val) and getVal(matrice,lig,col+1)!=2:
                            setVal(matrice,lig,col+1,1)

                    if col-1>0:
                        val=getVal(plateau,lig,col-1)
                        if passageOuest(case,val) and getVal(matrice,lig,col-1)!=2:
                            setVal(matrice,lig,col-1,1)

                if getVal(matrice,ligA,colA)==1:
                    return True

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
    ligne=getNbLignes(plateau)
    colone=getNbColonnes(plateau)

    matrice=Matrice(ligne,colone)

    setVal(matrice,ligD,colD,1)

    liste=[]
    pasArrive=True

    if not accessible(plateau,ligD,colD,ligA,colA):
        return None

    for i in range(ligne*colone):
        for lig in range(ligne):
            for col in range(colone):
                if getVal(matrice,lig,col)==1:

                    case=getVal(plateau,lig,col)
                    setVal(matrice,lig,col,2)
                    liste.append((lig,col))


                    if lig-1>0:
                        val=getVal(plateau,lig-1,col)
                        if passageNord(case,val) and getVal(matrice,lig-1,col)!=2:
                            setVal(matrice,lig-1,col,1)
                            if getVal(matrice,ligA,colA)==1:
                                liste.append((lig,col))
                                break


                    if lig+1<colone:
                        val=getVal(plateau,lig+1,col)
                        if passageSud(case,val) and getVal(matrice,lig+1,col)!=2:
                            setVal(matrice,lig+1,col,1)
                            if getVal(matrice,ligA,colA)==1:
                                liste.append((lig,col))
                                break

                    if col+1<ligne:
                        val=getVal(plateau,lig,col+1)
                        if passageEst(case,val) and getVal(matrice,lig,col+1)!=2:
                            setVal(matrice,lig,col+1,1)
                            if getVal(matrice,ligA,colA)==1:
                                liste.append((lig,col))
                                break

                    if col-1>0:
                        val=getVal(plateau,lig,col-1)
                        if passageOuest(case,val) and getVal(matrice,lig,col-1)!=2:
                            setVal(matrice,lig,col-1,1)
                            if getVal(matrice,ligA,colA)==1:
                                liste.append((lig,col))
                                break

                if getVal(matrice,ligA,colA)==1:
                    break
            if getVal(matrice,ligA,colA)==1:
                break
        if getVal(matrice,ligA,colA)==1:
            break

    chemin=[]
    j=True
    for i in range(-1,-len(liste),-1):
        if j:
            j=False
            val=liste[-1]
            chemin.append(val)
        else:
            if liste[i][0]==val[0] and (liste[i][1]==val[1]+1 or liste[i][1]==val[1]-1):
                chemin.append(liste[i])
                val=liste[i]
            elif (liste[i][0]==val[0]+1 or liste[i][0]==val[0]-1) and liste[i][1]==val[1]:
                chemin.append(liste[i])
                val=liste[i]

    if (ligD,colD) not in chemin:
        chemin.append((ligD,colD))
    chemin.reverse()
    if (ligA,colA) not in chemin:
        chemin.append((ligA,colA))

    return chemin


if __name__=="__main__":
    plat=Plateau(4,30)
    lig=getNbLignes(plat[0])
    col=getNbColonnes(plat[0])
    mat=Matrice(lig,col)
    for i in range(lig):
        for j in range(col):
            setVal(mat,i,j,listeCartes[coderMurs(plat[0][i][j])])
    for ligne in mat:
        print(ligne)
    print(getTresor(plat[0][0][3]))
    b=accessibleDist(plat[0],4,5,5,4)
    print(b)
