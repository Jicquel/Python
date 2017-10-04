#!/usr/bin/env python3
"""
Dessine un echiquier
"""

from random import randint
from cercle import Cercle


def ecrire_entete(largeur, hauteur, file):
    """
    Ecrit l'entête du fichier pgm
    """
    print("P2", file=file)
    print("{} {}".format(largeur, hauteur), file=file)
    print("255", file=file)


def demander_dimensions():
    """
    Demande les dimensions de l'image à l'utilisateur
    """
    return input("largeur : "), input("hauteur : ")


def ecrire_nuances_noir(file, cercle_un, cercle_deux, largeur, hauteur):
    """
    Remplit le fichier pgm de nuances de noir en fonction de la position
    des cercles
    """
    for ligne in range(int(hauteur)):
        for col in range(int(largeur)):
            if cercle_un.point_est_dans_cercle(int(col), int(ligne)) or\
                    cercle_deux.point_est_dans_cercle(int(col), int(ligne)):
                print("{} ".format(randint(0, 255)), file=file, end="")
            else:
                print("255 ", file=file, end="")
        print("", file=file)


def main():
    """
    main
    """
    with open("pgmImage.pgm", "w") as file:
        largeur, hauteur = demander_dimensions()
        ecrire_entete(largeur, hauteur, file)
        cercle_un = Cercle()
        cercle_un.set_param_aleatoirement(largeur, hauteur)
        cercle_deux = Cercle()
        cercle_deux.set_param_aleatoirement(largeur, hauteur)
        ecrire_nuances_noir(file, cercle_un, cercle_deux, largeur, hauteur)


main()
