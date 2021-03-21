###############################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Mar 20, 2021
# Description This program draws Archimedes Spirals using turtle module
###############################################################################

from turtle import *
from math import sin, cos, pi

def main():
    # Don't change this block -------------------------------------------------
    setup(564, 564)
    width('5')
    speed(10)
    # -------------------------------------------------------------------------

    xComprehensive = 0
    yComprehensive = 0

    rotation = 7

    for degree in range(2250):
        radian = degree * (pi / 180)
        xPosition = (radian / 10) * cos(radian)
        xComprehensive = xComprehensive + xPosition
        yPosition = (radian / 10) * sin(radian)
        yComprehensive = yComprehensive + yPosition
        goto(xComprehensive + xPosition, yComprehensive + yPosition)


    # Write your mainline logic here ------------------------------------------


# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
