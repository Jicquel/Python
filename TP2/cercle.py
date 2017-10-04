#!/usr/bin/env python
"""
cercle avec pour coordonnées (x,y) et un rayon r
"""

from random import randint
from math import sqrt


class Cercle:
    """
    Cercle avec pour coordonnées (x,y) et un rayon r
    """

    def __init__(self, x=0, y=0, rayon=0):
        """
        initialise les coordonnées à (0,0)
        """
        self.x = int(x)
        self.y = int(y)
        self.rayon = int(rayon)

    def set_param_aleatoirement(self, largeur, hauteur):
        """
        assigne les coordonnées et le rayon aléatoirement en prenant en compte
        la largeur et la hauteur maximale
        """
        self.x = randint(0, int(largeur)-1)
        self.y = randint(0, int(hauteur)-1)

        rayon_x_max = min(int(largeur)-self.x, self.x)
        rayon_y_max = min(int(hauteur)-self.y, self.y)
        self.rayon = randint(0, min(rayon_x_max, rayon_y_max))

        assert self.rayon >= 0

    def point_est_dans_cercle(self, px, py):
        """
        Indique si le point (px,py) est dans le cercle
        """
        return (self.x-px)*(self.x-px) + (self.y-py)*(self.y-py)\
            <= (self.rayon*self.rayon)

