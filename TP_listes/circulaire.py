#!/usr/bin/env python3
"""
listes triees, circulaires avec sentinelle.
"""

class Cellule:
    """
    valeur + suivant
    """
    #pylint: disable=too-few-public-methods
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class Liste:
    """
    liste circulaire triee, simplement chainee avec sentinelle.
    """
    def __init__(self, sentinelle, iterable=None):
        """
        remplit la liste avec les elements de l'iterable donne.
        'sentinelle' precise la valeur de la cellule sentinelle
        pre-condition: l'iterable donne est trie.
        """
        
        self.tete = Cellule(sentinelle)
        cel_prec = self.tete
        for value in iterable:
            if type(value) is Cellule:
                cel_prec.suivant = value
            else:
                cel_prec.suivant = Cellule(value)
            cel_prec = cel_prec.suivant
        cel_prec.suivant = self.tete
        
    def cellules(self, inclure_sentinelle=False):
        """
        renvoie un iterateur sur toutes les cellules de la liste.
        'inclure_sentinelle' est un booleen permettant de preciser
        si la sentinelle est inclue ou non dans les cellules iterees.
        """
        if inclure_sentinelle:
            yield self.tete
        cel = self.tete.suivant
        while cel != self.tete:
            yield cel
            cel = cel.suivant

    def decoupe(self):
        """
        coupe la liste en 2 (une cellule sur 2).
        par exemple (1,4,2,3,5) devient (1,2,5) et (4,3).
        renvoie les deux nouvelles listes.
        aucune nouvelle cellule n'est creee.
        """
        cellules_liste_1 = [cel for index, cel in enumerate(self.cellules())
                            if not bool(index % 2)]
        cellules_liste_2 = [cel for index, cel in enumerate(self.cellules())
                            if bool(index % 2)]
        return Liste(self.tete.valeur, cellules_liste_1),\
            Liste(self.tete.valeur, cellules_liste_2)

    def ajouter(self, valeur):
        """
        ajoute la valeur donnee a la bonne place dans la liste.
        """
        cel_a_rajouter = Cellule(valeur)
        cel_prec = self.tete
        for cel in self.cellules():
            if cel.valeur > valeur:
                cel_prec.suivant, cel_a_rajouter.suivant = cel_a_rajouter,\
                    cel_prec.suivant
                return
            cel_prec = cel
        cel_prec.suivant, cel_a_rajouter.suivant = cel_a_rajouter,\
            cel_prec.suivant

    def supprimer(self, valeur):
        """
        supprime la premiere cellule contenant la valeur donnee.
        """
        cel_prec = self.tete
        for cel in self.cellules():
            if cel.valeur == valeur:
                cel_prec.suivant = cel.suivant
                return

    def __str__(self):
        string = ""
        for cel in self.cellules():
            string+=str(cel.valeur)+" "
        return string


def test():
    """
    tests simples des differentes methodes.
    """
    entiers = Liste(float("inf"), range(8))
    pairs, impairs = entiers.decoupe()
    print(pairs, impairs)
    pairs.supprimer(4)
    pairs.supprimer(0)
    pairs.supprimer(2)
    pairs.supprimer(6)
    impairs.ajouter(6)
    impairs.ajouter(0)
    print(pairs, impairs)


if __name__ == "__main__":
    test()
