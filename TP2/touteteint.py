#!/usr/bin/env python
"""
Implémente le jeu tout éteint
"""

import sys
from colorama import init, Fore


class Plateau:
    """
    représente le plateau de jeu
    """

    def __init__(self):
        """
        largeur et hauteur du plateau de jeu
        """
        self.largeur = 0
        self.hauteur = 0
        self.valeurs = []

    def afficher(self):
        """
        affiche le plateau de jeu sous format svg
        """
        for col in range(self.largeur):
            print(chr(col+65))

    def initialiser_dimensions(self, name_of_file):
        """
        initialise les dimensions du plateau de jeu
        """

        hauteur, largeur = sum(1 for line in open(name_of_file, "r")), \
            len(open(name_of_file).readline().split()[0])

        self.largeur = largeur
        self.hauteur = hauteur
        self.valeurs = [[False for _ in range(self.hauteur)] for
                        _ in range(self.largeur)]

    def charger_plateau(self, name_of_file):
        """
        charge le plateau d'un niveau de jeu
        """

        self.initialiser_dimensions(name_of_file)

        num_col, num_ligne = 0, 0
        with open(name_of_file) as file:
            for line in file:
                line = line.split()[0]
                for char in line:
                    var = bool(char == '.')
                    self.valeurs[num_ligne][num_col] = var

                    num_col += 1
                num_ligne += 1
                num_col = 0


def main():
    """
    main
    """

    if len(sys.argv) != 2 or sys.argv[0] == "-h" or sys.argv[0] == "--help":
        print("utilisation:", sys.argv[0], " niveau.txt")
        sys.exit(1)

    init()
    print(Fore.BLUE + 'blue text on stderr')
    plateau = Plateau()
    plateau.charger_plateau(sys.argv[1])
    plateau.afficher()




main()
