#!/usr/bin/env python
"""
Dessine un echiquier
"""


def dessiner_echiquier(width):
    """
    crée le svg d'un echiquier
    """
    print("<svg width='{}' height='{}'>".format(width, width))

    taille_case = int(width/8)

    for ligne in range(8):
        for col in range(8):
            if (col + (ligne % 2)) % 2 == 0:
                print("<rect x='{}' y='{}' width='{}' height='{}'\
  style=\"fill:white\" />".format(col*taille_case, ligne*taille_case,
                                  taille_case, taille_case))
            else:
                print("<rect x='{}' y='{}' width='{}' height='{}'\
  style=\"fill:black\" />".format(col*taille_case, ligne*taille_case, 
                                  taille_case, taille_case))

    print("</svg>")


def main():
    """
    main
    """
    dessiner_echiquier(500)

main()
