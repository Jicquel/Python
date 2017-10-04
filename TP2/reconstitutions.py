#!/usr/bin/env python
"""
Lit des points, puis les stocke en svg
"""

from point import Point


def main():
    """
    main
    """

    print("<svg width=\"1000\" height=\"1000\">")
    for _ in range(1000):
        point = Point()
        point.set_coords()
        point.draw_svg()

    print("</svg>")


main()
