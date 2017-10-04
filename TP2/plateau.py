#!/usr/bin/env python3
"""
Dessine un plateau de jeu de l'oie
"""

import svg

class Plateau:
    """
    Dessine un plateau du jeu de l'oie
    """

    def __init__(self, largeur=650, hauteur=600):
        """
        largeur de l'image, hauteur de l'image, direction initiale
        du jeu
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.direction_droite = True
        self.direction_haut = False
        self.cote_carre = 40

    def afficher_plateau(self):
        """
        Affiche le fichier sous format svg
        """
        svg.entete(self.largeur, self.hauteur)

        nombre_bloc_x = self.largeur//self.cote_carre
        x, y = 0, self.hauteur-self.cote_carre
        num_bloc = 1
        droite = True

        while y >= 0:
            self.dessiner_carre(x, y, num_bloc)
            num_bloc += 1
            for _ in range(nombre_bloc_x-1):
                x += int(droite)*self.cote_carre-int(not droite)*self.cote_carre
                self.dessiner_carre(x, y, num_bloc)
                num_bloc += 1
            if y-2*self.cote_carre >= 0:
                y -= self.cote_carre
                self.dessiner_carre(x, y, num_bloc)
                num_bloc += 1
                y -= self.cote_carre
                self.dessiner_carre(x, y, num_bloc)
            else:
                y -= 2*self.cote_carre
            droite = not droite

        svg.pied()

    def dessiner_carre(self, x, y, num_bloc):
        print("<polygon points=\"{},{},{},{},{},{},{},{}\" style=\"\
              stroke_width:1;stroke:black\"/>".format(
                  x, y,
                  x+self.cote_carre, y,
                  x+self.cote_carre, y+self.cote_carre,
                  x, y+self.cote_carre))
        print("<text x=\"{}\" y=\"{}\" fill=\"red\">{}</text>".
              format(x+2,
                     y+self.cote_carre-5,
                     num_bloc))


def main():
    """
    main
    """
    p = Plateau()
    p.afficher_plateau()

main()
