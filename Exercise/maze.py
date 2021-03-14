################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 14, 2021
# Description This program shows how the turtle on the center escape the maze
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width('5')
    step = 12
    # --------------------------------------------------------------------------

    # Write your code here
    forward(10)
    setheading(90)
    forward(35)
    setheading(0)
    forward(25)
    setheading(90)
    forward(72)
    setheading(180)
    forward(25)
    setheading(90)
    forward(100)
    setheading(0)
    forward(25)
    setheading(90)
    forward(20)
    setheading(0)
    forward(195)
    setheading(270)
    forward(225)
    setheading(0)
    forward(15)

# Don't change this
if __name__ == '__main__':
    main()
    done()
