#!/usr/bin/env python3
"""
Plus grande sous-suite monotone
"""

import sys


class Suite:
    """
    Dessine un plateau du jeu de l'oie
    """

    def __init__(self, elements=[]):
        """
        elements dont est comoposée la liste
        """
        self.elements = elements

    def afficher_plateau(self):
        """
        Affiche le fichier sous format svg
        """


def iter_elements(file_name):
    """
    itère sur les éléments d'un fichier
    """
    file = open(file_name, "r")
    elements = file.read().split()
    for element in elements:
        yield element


def iter_sous_suite_monotones(file_name):
    """
    itère sur toutes les plus grandes suites monotones.
    """

    ancien_indice, indice_actuel = 0, 0
    iter_finie = False

    while not iter_finie:
        res = []
        indice_actuel = 0
        sous_suite_finie = False
        facteur = 0
        dernier_nombre_res = 0

        for e in iter_elements(file_name):
            if not sous_suite_finie:
                if indice_actuel == ancien_indice:
                    res.append(int(e))
                    dernier_nombre_res = int(e)

                elif indice_actuel == ancien_indice+1:
                    res.append(int(e))
                    dernier_nombre_res = int(e)
                    facteur = res[0]-res[1]

                elif indice_actuel > ancien_indice+1:
                    # si ne respecte pas monotonie
                    if (dernier_nombre_res-int(e))*facteur < 0:
                        sous_suite_finie = True
                    else:
                        res.append(int(e))
                        dernier_nombre_res = int(e)

                if not sous_suite_finie:
                    indice_actuel += 1

        if ancien_indice == indice_actuel-1:
            iter_finie = True

        ancien_indice = indice_actuel-1
        yield res


def main():
    """
    main
    """
    if len(sys.argv) != 2 or sys.argv[0] == "-h" or sys.argv[0] == "--help":
        print("utilisation: {} {}".format(sys.argv[0], "file_to_read"))
        sys.exit(1)

    print(max(iter_sous_suite_monotones(sys.argv[1]),key=len))
main()
