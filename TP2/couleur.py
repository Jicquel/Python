#!/usr/bin/env python
"""
Couleur rgb
"""

from random import randint


class Couleur:
    """
    couleur
    """

    def __init__(self, red=0, green=0, blue=0):
        """
        initialise les composantes rgb
        """
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        """
        affiche la couleur sous format rgb
        """
        return "rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")"

    @staticmethod
    def couleur_random():
        """
        retourne une couleur aléatoire
        """
        return Couleur(randint(0, 256),
                       randint(0, 256),
                       randint(0, 256))

    def rotation_autour(self, centre, angle):
        """
        effectue une rotation du triangle par 
        rapport au centre un certain angle
        """
        self.point1.rotation_autour_point(centre, angle)
        self.point2.rotation_autour_point(centre, angle)
        self.point3.rotation_autour_point(centre, angle)

