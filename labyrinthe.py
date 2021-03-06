# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module labyrinthe
   ~~~~~~~~~~~~~~~~~

   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *
import copy


def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    if nbTresors<12:
        nbTresors=12
    elif nbTresors>49:
        nbTresor=49


    joueurs=ListeJoueurs(nomsJoueurs)
    initAleatoireJoueurCourant(joueurs)
    distribuerTresors(joueurs,nbTresors,nbTresorsMax)
    val=getNbJoueurs(joueurs)
    labyrinthe={"Joueurs":joueurs,"tresors":nbTresors,"plateau":Plateau(val,nbTresors),"phase":1,"coupsInterdit":(-1,"0")}

    return labyrinthe

def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return getMatrice(labyrinthe["plateau"])

def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return getNbJoueurs(labyrinthe["Joueurs"])


def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return nomJoueurCourant(labyrinthe["Joueurs"])

def getTypeJoueurCourant(labyrinthe):
    """
    retourne le type du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le type du joueurs courant
    """
    return typeJoueurCourant(labyrinthe["Joueurs"])


def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return numJoueurCourant(labyrinthe["Joueurs"])

def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """
    return labyrinthe["phase"]


def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    labyrinthe["phase"]+=1
    if labyrinthe["phase"]>=3:
        labyrinthe["phase"]=1


def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """
    return labyrinthe["tresors"]

def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py
    """
    return labyrinthe["Joueurs"]


def enleverTresor(labyrinthe,lin,col,numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe.
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    labyrinthe["tresors"]-=1
    prendreTresorPlateau(getPlateau(labyrinthe),lin,col,numTresor)


def prendreJoueurCourant(labyrinthe,lin,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    joueur = getJoueurCourant(labyrinthe["Joueurs"])
    prendrePionPlateau(getPlateau(labyrinthe),lin,col,joueur)


def poserJoueurCourant(labyrinthe,lin,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    joueur = getJoueurCourant(labyrinthe["Joueurs"])
    poserPionPlateau(getPlateau(labyrinthe),lin,col,joueur)

def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer
    """
    return getCarte(labyrinthe["plateau"])


def coupInterdit(labyrinthe,direction,rangee):
    """
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    if direction in ("N","S") and labyrinthe["coupsInterdit"][1] in ("N","S") and rangee == labyrinthe["coupsInterdit"][0] and direction not in labyrinthe["coupsInterdit"][1]:
        return True

    elif direction in ("E","O") and labyrinthe["coupsInterdit"][1] in ("E","O") and rangee == labyrinthe["coupsInterdit"][0] and direction not in labyrinthe["coupsInterdit"][1]:
        return True

    return False

def jouerCarte(labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées
    en paramètres. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    if direction=="N":
        carte=decalageColonneEnBas(getPlateau(labyrinthe),rangee,getCarteAJouer(labyrinthe))
    elif direction=="S":
        carte=decalageColonneEnHaut(getPlateau(labyrinthe),rangee,getCarteAJouer(labyrinthe))
    elif direction=="E":
        carte=decalageLigneAGauche(getPlateau(labyrinthe),rangee,getCarteAJouer(labyrinthe))
    elif direction=="O":
        carte=decalageLigneADroite(getPlateau(labyrinthe),rangee,getCarteAJouer(labyrinthe))

    changerCarte(labyrinthe["plateau"],carte)


def tournerCarte(labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyritnthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
    """
    if sens=="H":
        tournerHoraire(getCarteAJouer(labyrinthe))
    elif sens=="A":
        tournerAntiHoraire(getCarteAJouer(labyrinthe))

def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyritnthe: le labyrinthe considéré
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return tresorCourant(labyrinthe["Joueurs"])

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyritnthe: le labyrinthe considéré
    resultat: les coordonnées du trésor à chercher ou None si celui-ci
              n'est pas sur le plateau
    """
    tres=tresorCourant(labyrinthe["Joueurs"])
    return getCoordonneesTresor(getPlateau(labyrinthe),tres)


def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyritnthe: le labyrinthe considéré
    resultat: les coordonnées du joueur courant ou None si celui-ci
              n'est pas sur le plateau
    """
    jou=numJoueurCourant(labyrinthe["Joueurs"])
    return getCoordonneesJoueur(getPlateau(labyrinthe),jou)


def executerActionPhase1(labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    if action=="T" or action == "T T":
        tournerCarte(labyrinthe)
        return 0
    elif action in ["N","E","S","O"] and rangee in [1,3,5]:
        if coupInterdit(labyrinthe,action,rangee):
            return 2
        else:
            jouerCarte(labyrinthe,action,rangee)
            changerPhase(labyrinthe)
            labyrinthe["coupsInterdit"]=(action,rangee)
            return 1
    elif (action and rangee) in ["0","1","2","3","4","5","6","7","8","9"]:
        return 3
    else:
        return 4

def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    try:
        val0,val1 = getCoordonneesJoueurCourant(labyrinthe)
    except:
        return None
    return accessibleDist(getPlateau(labyrinthe),val0,val1,ligA,colA)


def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    tresC = getTresorCourant(labyrinthe)
    coordJoueur = getCoordonneesJoueurCourant(labyrinthe)
    coordTres = getCoordonneesTresorCourant(labyrinthe)

    if coordJoueur == coordTres and type(coordJoueur) == type(coordTres) and coordTres!=None:
        joueurCourantTrouveTresor(labyrinthe["Joueurs"])
        prendreTresorPlateau(getPlateau(labyrinthe),coordTres[0],coordTres[1],tresC)
        if joueurCourantAFini(labyrinthe["Joueurs"]):
            return 2
        else:
            changerJoueurCourant(labyrinthe["Joueurs"])
            changerPhase(labyrinthe)
            return 1
    else:
        changerJoueurCourant(labyrinthe["Joueurs"])
        changerPhase(labyrinthe)
        return 0


def labyrintheIA(labyrinthe):
    """
    L'IA du jeu du labyrinthe
    """
    dir=["N","S","E","O"]
    ran=[1,3,5]

    try:
        tresorX,tresorY=getCoordonneesTresorCourant(labyrinthe)
    except:
        tresorX=getCoordonneesTresorCourant(labyrinthe)

    cj=getCoordonneesJoueurCourant(labyrinthe)

    if getPhase(labyrinthe)==1 and getCoordonneesTresorCourant(labyrinthe)!=None and cj!=None:
        for h in range(4):
            tournerCarte(labyrinthe)
            for i in dir:
                for j in ran:
                    labyV=copy.deepcopy(labyrinthe)
                    if not coupInterdit(labyrinthe,i,j):
                        val=executerActionPhase1(labyV,i,j)
                        if accessibleDistJoueurCourant(labyV,tresorX,tresorY)!=None and getCoordonneesTresorCourant(labyrinthe)!=None and val==1:
                            return i,j

        while True:
            i=random.choice(dir)
            j=random.choice(ran)
            if not coupInterdit(labyrinthe,i,j):
                return i,j

    elif getPhase(labyrinthe)==1 and cj!=None:
        for h in range(4):
            tournerCarte(labyrinthe)
            for i in dir:
                for j in ran:
                    labyV=copy.deepcopy(labyrinthe)
                    if not coupInterdit(labyrinthe,i,j):
                        val=executerActionPhase1(labyV,i,j)
                        try:
                            tresorX,tresorY=getCoordonneesTresorCourant(labyV)
                            acc=accessibleDistJoueurCourant(labyV,tresorX,tresorY)
                        except:
                            tresorX=getCoordonneesTresorCourant(labyV)
                            acc=None
                        if acc!=None and tresorX!=None and val==1:
                            return i,j

        while True:
            i=random.choice(dir)
            j=random.choice(ran)
            if not coupInterdit(labyrinthe,i,j):
                return i,j


    elif getPhase(labyrinthe)==1:
        while True:
            i=random.choice(dir)
            j=random.choice(ran)
            if not coupInterdit(labyrinthe,i,j):
                return i,j

    elif cj==None and getPhase(labyrinthe)==2:
        return None

    elif tresorX!=None and accessibleDistJoueurCourant(labyrinthe,tresorX,tresorY)!=None and cj!=None and getCoordonneesTresorCourant(labyrinthe)!=None and getPhase(labyrinthe)==2:
        return tresorX,tresorY

    elif getPhase(labyrinthe)==2:
        plat=getPlateau(labyrinthe)
        while True:
            i=random.randint(0,getNbLignes(plat)-1)
            j=random.randint(0,getNbColonnes(plat)-1)
            if accessibleDistJoueurCourant(labyrinthe,i,j):
                return i,j


if __name__ ==  "__main__":
    laby=Labyrinthe(["a","b","c","d"])
    a=getPlateau(laby)
    b=getCarteAJouer(laby)
    getCoordonneesJoueurCourant(laby)
    enleverTresor(laby,1,1,5)
    jouerCarte(laby,"S",5)
