# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~

   Ce module gère la liste des joueurs.
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    listeDesJoueurs={"joueurs":[],"courant":0}
    for nom in nomsJoueurs:
        listeDesJoueurs["joueurs"].append(Joueur(nom))

    return listeDesJoueurs


def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs["joueurs"].append(joueur)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    val=getNbJoueurs(joueurs)
    joueurs["courant"]=random.randint(0,val)

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    val=getNbJoueurs(joueurs)
    joueurs=joueurs["joueurs"]
    if nbTresorMax==0:
        nbTresorMax=int(nbTresors/val)

    liste=[k for k in range(1,nbTresors+1)]
    random.shuffle(liste)

    for jou in joueurs:
        for t in range(nbTresorMax):
            ajouterTresor(jou,liste.pop())



def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    val=joueurs["courant"]
    val+=1
    if joueurs["courant"]>=val:
        val=0


def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs["joueurs"])

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    val=joueurs["courant"]
    return joueurs["joueurs"][val]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs=getJoueurCourant(joueurs)
    tresorTrouve(joueurs)

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    joueurs=joueurs["joueurs"][numJoueur]
    return getNbTresorsRestants(joueurs)


def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs["courant"]

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    joueur=getJoueurCourant(joueurs)
    return getNom(joueur)


def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nom du joueur numJoueur
    """
    joueur=joueurs["joueurs"][numJoueur]
    return getNom(joueur)

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    joueur=joueurs["joueurs"][numJoueur]
    return prochainTresor(joueur)

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le prochain trésor du joueur courant (un entier)
    """
    joueur=getJoueurCourant(joueurs)
    return prochainTresor(joueur)

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs
    résultat: un booleen indiquant si le joueur courant a fini
    """
    val = numJoueurCourant(joueurs)
    test = nbTresorsRestantsJoueur(joueurs,val)
    if test!=0:
        return False
    return True

if __name__ == "__main__":
    j=ListeJoueurs(["a","b","c","d"])
    distribuerTresors(j)
    #v=prochainTresorJoueur(j,2)
    #w=nbTresorsRestantsJoueur(j,1)
    #x=getJoueurCourant(j)
    #y=nomJoueur(j,1)
    print(j)#,v,w,x,y)
