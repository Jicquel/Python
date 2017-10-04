#!/usr/bin/env python
"""
triangle
"""

from random import randint
from point import Point


class Triangle:
    """
    Triangle avec trois coordonnées Point
    """

    def __init__(self, point1, point2, point3):
        """
        initialise les coordonnées à (0,0)
        """
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def rotation_autour(self, centre, angle):
        """
        effectue une rotation du triangle par
        rapport au centre un certain angle
        """
        p1_new = self.point1.rotation_autour_point(centre, angle)
        p2_new = self.point2.rotation_autour_point(centre, angle)
        p3_new = self.point3.rotation_autour_point(centre, angle)

        return Triangle(p1_new, p2_new, p3_new)


def triangle_aleatoire(tab_x, tab_y):
    """
    assigne les coordonnées des points du triangle
    dans le carré x_min, x_max, y_min, y_max
    """
    x_min = tab_x[0]
    x_max = tab_x[1]
    y_min = tab_y[0]
    y_max = tab_y[1]
    point1 = Point([randint(x_min, x_max+1), randint(y_min, y_max+1)])
    point2 = Point([randint(x_min, x_max+1), randint(y_min, y_max+1)])
    point3 = Point([randint(x_min, x_max+1), randint(y_min, y_max+1)])

    return Triangle(point1, point2, point3)
