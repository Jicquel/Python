#!/usr/bin/env python3
"""
listes simplements chainees + quelques operations
"""
from tycat import trace


class Cellule:
    """
    une cellule d'une liste. contient une valeur et un pointeur
    vers la cellule suivante.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant


class Liste:
    """
    une liste simplement chainee.
    contient un pointeur sur la cellule en tete de liste et un autre sur
    la queue de liste.
    un compteur permet de savoir rapidement la taille de la liste.
    """
    def __init__(self):
        self.tete = None
        self.queue = None
        self.taille = 0

    #@trace
    def ajouter_en_tete(self, valeur):
        """
        ajoute une cellule en tete. cout : O(1).
        """
        cel = Cellule(valeur)
        if self.tete is None:
            self.tete, self.queue = cel, cel
        else:
            cel.suivant, self.tete = self.tete, cel
        self.taille += 1


    #@trace
    def ajouter_en_queue(self, valeur):
        """
        ajoute une cellule en queue. cout : O(1).
        on peut le faire rapidement grace au pointeur de queue.
        """
        cel = Cellule(valeur)
        if self.tete is None:
            self.tete, self.queue = cel, cel
        else:
            self.queue.suivant, self.queue = cel, cel
        self.taille += 1

    def cellules(self):
        """
        iterateur sur chaque cellule.
        """
        cellule = self.tete
        while cellule is not None:
            yield cellule
            cellule = cellule.suivant

    def recherche(self, valeur):
        """
        renvoie la premiere cellule contenant la valeur donnee.
        """
        for cel in self.cellules():
            if cel.valeur == valeur:
                return cel

    #@trace
    def supprimer(self, valeur):
        """
        enleve la premiere cellule contenant la valeur donnee.
        """

        cel_prec = None
        for cel in self.cellules():
            if cel.valeur == valeur:
                if cel_prec is None:
                    self.tete = cel.suivant
                    self.taille -= 1
                    if self.taille == 0:
                        self.queue = None
                else:
                    cel_prec.suivant = cel.suivant
                    self.taille -= 1
                    if cel_prec.suivant is None:
                        self.queue = cel_prec
                return
            cel_prec = cel

    def __str__(self):
        """
        affiche (val1, val2, val3....)
        """
        num_valeur = 1
        my_str = "("
        for cel in self.cellules():
            my_str = my_str+str(cel.valeur)
            if self.taille > num_valeur:
                my_str = my_str+", "
            num_valeur += 1
        my_str = my_str+")"
        return my_str


def test_listes():
    """
    on teste toutes les operations de base, dans differentes configurations.
    """
    exemple = Liste()
    exemple.ajouter_en_tete(3)
    exemple.ajouter_en_tete(5)
    exemple.ajouter_en_queue(2)
    exemple.ajouter_en_queue(4)
    print("exemple : ", exemple)
    print("recherche : ", exemple.recherche(3).valeur)
    print("adresses des cellules : ",
          ",".join([hex(id(c))for c in exemple.cellules()]))
    exemple.supprimer(5)
    print("apres suppression de 5 : ", exemple)
    exemple.supprimer(4)
    print("apres suppression de 4 : ", exemple)

if __name__ == "__main__":
    test_listes()
