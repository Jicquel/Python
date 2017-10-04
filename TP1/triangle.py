#!/usr/bin/env python3

"""
Affiche un triangle sous forme de 3 disques.
"""

from random import randint
from os import system


class Point:
    """
    (x,y)
    """
    def __init__(self, x, y):
        """
        constructeur
        """
        self.x = x
        self.y = y


def set_points_triangle():
    """
    Demande un entier sur la ligne de commande
    """
    return [Point(randint(0, 500), randint(0, 500)),
            Point(randint(0, 500), randint(0, 500)),
            Point(randint(0, 500), randint(0, 500))]


def afficher_triangle_disque(points, width, height):
    """
    Affiche le triangle sous forme de disque
    """
    with open("triangle.svg", "w") as fichier_svg:
        print("<svg width='{}' height='{}'>".format(width, height),
              file=fichier_svg)
        for point in points:
            print("<circle cx='{}' cy='{}' r='20' fill='{}'/>".format(point.x,
                                                                      point.y,
                                                                      "blue"),
                  file=fichier_svg)
        print("</svg>", file=fichier_svg)
    system("tycat triangle.svg")


def main():
    """
    Partie principale
    """
    afficher_triangle_disque(set_points_triangle(), 600, 600)

main()
