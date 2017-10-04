#!/usr/bin/env python
"""
svg
"""

from couleur import Couleur 


def entete(largeur, hauteur):
    """
    affiche l'entete de svg
    """
    print("<svg height=\"{}\" width=\"{}\">".format(hauteur, largeur))


def affiche_triangle(triangle, couleur):
    """
    affiche un triangle de couleur 'couleur'
    """
    print("<polygon points=\"{},{} {},{} {},{}\" style=\"fill:{};\" />".format(
        triangle.point1.x, triangle.point1.y,
        triangle.point2.x, triangle.point2.y,
        triangle.point3.x, triangle.point3.y,
        str(couleur)))


def pied():
    """
    affiche la fin du fichier svg
    """
    print("</svg>")


def couleur_aleatoire():
    """
    renvoie une couleur aléatoire
    """

    return Couleur.couleur_random()

