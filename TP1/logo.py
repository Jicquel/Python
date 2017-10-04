"""
le module implemente les primitives graphiques basiques
d'une tortue logo.
"""
from math import sin, cos, pi


class Logo:
    """
    une tortue logo, positionnee dans le plan.
    """
    def __init__(self):
        """
        positionne la tortue a l'origine, demarre le svg
        """
        self.abscisse = 0.0
        self.ordonnee = 0.0
        self.direction = 270.0  # angle du regard de la tortue (en degre)
        self.crayon_en_bas = False
        # en tete du fichier svg
        print("<svg width=\"100\" height=\"100\">")

    def avance(self, distance):
        """
        avance la tortue tout droit de la distance donnee
        """
        x_final = cos(self.direction*pi/180)*distance+self.abscisse
        y_final = sin(self.direction*pi/180)*distance+self.ordonnee

        if x_final < 0:
            x_final = 0
        if y_final < 0:
            y_final = 0

        if self.crayon_en_bas:
            print("<line x1='{}' y1='{}' x2='{}' y2='{}'\
            style=\"stroke:rgb(255, 0, 0);stroke-width:2\"\
             />".format(self.abscisse, self.ordonnee, x_final, y_final))
        self.abscisse = x_final
        self.ordonnee = y_final

    def tourne_droite(self, angle):
        """
        change la direction de la tortue en tournant a droite
        de l'angle donne (en degre)
        """
        self.direction += angle

    def tourne_gauche(self, angle):
        """
        change la direction de la tortue en tournant a gauche
        de l'angle donne (en degre)
        """
        self.direction -= angle

    def baisse_crayon(self):
        """
        baisse le crayon. a partir de maintenant la tortue dessine
        lorsqu'elle avance
        """
        self.crayon_en_bas = True

    def leve_crayon(self):
        """
        leve le crayon. a partir de maintenant la tortue ne dessine pas
        lorsqu'elle avance.
        """
        self.crayon_en_bas = False

    def __del__(self):
        """
        destructeur, termine le fichier svg
        """
        print("</svg>")

