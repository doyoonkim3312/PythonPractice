###############################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Mar 20, 2021
# Description This program draws 5 characters in random order. (Using turtle
# module)
###############################################################################

from turtle import *
import random as random
import vowels

# Add your imports here -------------------------------------------------------


def main():
    # Don't change this block -------------------------------------------------
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)
    # -------------------------------------------------------------------------

    letters = random.sample(range(5),5)
    for element in letters:
        if element == 0:
            vowels.draw_e()
        elif element == 1:
            vowels.draw_u()
        elif element == 2:
            vowels.draw_o()
        elif element == 3:
            vowels.draw_a()
        elif element == 4:
            vowels.draw_i()

        setheading(0)
        forward(15)

    # Write your mainline logic here ------------------------------------------



# Don't change this -----------------------------------------------------------

if __name__ == '__main__':
    main()
    done()
