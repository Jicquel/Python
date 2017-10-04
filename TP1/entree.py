#!/usr/bin/env python

"""
Demande l'age
"""

def entree():
    """
    Demande un entier sur la ligne de commande
    """
    return int(input("Entrez un nombre"))

def main():
    """
    Partie principale
    """
    somme = entree()+entree()
    print(somme)

main()
