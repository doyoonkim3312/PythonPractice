###############################################################################
# Author:
# Date:
# Description ...
###############################################################################

from turtle import *


def draw_a():
    penup()
    setheading(0)
    forward(60)
    setheading(90)
    pendown()
    forward(60)
    penup()
    setheading(270)
    forward(30)
    pendown()
    setheading(90)
    circle(30)
    penup()
    setheading(270)
    forward(30)
    setheading(0)



def draw_e():
    penup()
    setheading(90)
    forward(30)
    pendown()
    setheading(0)
    forward(60)
    setheading(90)
    circle(30, 315)
    penup()
    setheading(270)
    forward(8)
    setheading(0)
    forward(8)


def draw_i():
    forward(30)
    setheading(90)
    pendown()
    forward(60)
    penup()
    forward(20)
    pendown()
    dot(9)
    penup()
    setheading(270)
    forward(80)
    setheading(0)
    forward(30)



def draw_o():
    forward(30)
    pendown()
    circle(30)
    penup()
    forward(30)



def draw_u():
    setheading(90)
    forward(60)
    pendown()
    setheading(270)
    forward(30)
    circle(30, 180)
    penup()
    forward(30)
    pendown()
    setheading(270)
    forward(60)
    penup()
    setheading(0)


def main():

    # You can use this for your own testing.



# Don't change this -----------------------------------------------------------
    if __name__ == '__main__':
        main()
        done()
