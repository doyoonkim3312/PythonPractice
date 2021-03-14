################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 14, 2021
# Description This program draw 'Hello turtle' using Turtle module
################################################################################

# Don't change this
from turtle import *

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



def draw_h():
    pendown()
    setheading(90)
    forward(120)
    penup()
    setheading(270)
    forward(120)
    setheading(0)
    forward(60)
    setheading(90)
    pendown()
    forward(30)
    circle(30, 180)
    penup()
    setheading(270)
    forward(30)
    setheading(0)
    forward(60)


def draw_l():
    penup()
    forward(30)
    pendown()
    setheading(90)
    forward(120)
    penup()
    setheading(270)
    forward(120)
    setheading(0)
    forward(30)


def draw_o():
    forward(30)
    pendown()
    circle(30)
    penup()
    forward(30)


def draw_r():
    pendown()
    setheading(90)
    forward(60)
    penup()
    setheading(0)
    forward(30)
    pendown()
    setheading(180)
    circle(30,90)
    penup()
    forward(30)
    setheading(0)
    forward(60)


def draw_t():
    forward(30)
    pendown()
    setheading(90)
    forward(120)
    penup()
    setheading(270)
    forward(30)
    pendown()
    setheading(180)
    forward(30)
    penup()
    setheading(0)
    forward(30)
    pendown()
    forward(30)
    penup()
    setheading(270)
    forward(90)
    setheading(0)


def draw_u():
    setheading(90)
    forward(60)
    pendown()
    setheading(270)
    forward(30)
    circle(30,180)
    penup()
    forward(30)
    pendown()
    setheading(270)
    forward(60)
    penup()
    setheading(0)



def main():

    # Don't change this block --------------------------------------------------
    setup(600, 400)
    width(9)
    # --------------------------------------------------------------------------

    # Write your main function code here
    penup()
    goto(-200,50)
    draw_h()
    forward(20)
    draw_e()
    forward(20)
    draw_l()
    forward(20)
    draw_l()
    forward(20)
    draw_o()
    goto(-250, -120)
    draw_t()
    forward(20)
    draw_u()
    forward(30)
    draw_r()
    forward(10)
    draw_t()
    forward(20)
    draw_l()
    forward(20)
    draw_e()



# Don't change this
if __name__ == '__main__':
    main()
    done()
