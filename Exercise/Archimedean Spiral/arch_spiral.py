###############################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Mar 20, 2021
# Description This program draws Archimedes Spirals using turtle module.
###############################################################################

from turtle import *
from math import sin, cos, pi

def main():
    # Don't change this block -------------------------------------------------
    setup(564, 564)
    width('5')
    speed(10)
    # -------------------------------------------------------------------------

    #Formulas given in manual are used. Degree increasement scale is 0.58
    degree = 0
    while degree < 2160:
        radian = degree * (pi / 180)
        xPosition = (degree / 10) * cos(radian)
        yPosition = (degree / 10) * sin(radian)
        goto(xPosition, yPosition)
        degree = degree + 0.58


    # Write your mainline logic here ------------------------------------------


# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
