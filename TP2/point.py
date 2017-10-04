#!/usr/bin/env python
"""
Point avec pour coordonnées (x,y)
"""

from math import sin, cos


class Point:
    """
    Point avec pour coordonnées (x,y)
    """
    def __init__(self, tab=[0, 0]):
        """
        initialise les coordonnées à (x,y)
        """
        self.x = tab[0]
        self.y = tab[1]

    def set_coords(self):
        """
        assigne les coordonnées à partir d'input
        """
        self.x, self.y = input(), input()

    def draw_svg(self):
        """
        affiche le svg du point
        """
        print("<circle cx='{}' cy='{}' r=\"1\"/>".format(self.x, self.y))

    def rotation_autour_point(self, centre, angle):
        """
        Effectue une rotation du point autour du point 'centre' avec
        l'angle 'angle'
        """
        x_apres_modif = (self.x-centre.x)*cos(angle) - \
            (self.y-centre.y)*sin(angle)+centre.x
        y_apres_modif = (self.x-centre.x)*sin(angle) + \
            (self.y-centre.y)*cos(angle)+centre.y
        return Point([x_apres_modif, y_apres_modif])
