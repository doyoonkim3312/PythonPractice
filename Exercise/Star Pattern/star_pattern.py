################################################################################
# Author: 
# Date: 
# Description ...
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()
    # --------------------------------------------------------------------------

    # Write your code here
    color('black','pink')
    begin_fill()

    points = int(input("How many points do you want?: "))
    angle = 360 / points
    speed(10)

    for line in range(points * 2):
        if line == 0:
            right(90 - angle)
            forward(side_length)
        elif (line + 1) % 2 == 0:
            left(180 - angle)
            forward(side_length)
        else:
            right(180 - (2 * angle))
            forward(side_length)
    end_fill()


# Don't change this
if __name__ == '__main__':
    main()
    done()
