from turtle import *

forward(100)
bgcolor('#cfb991')

left(90)
forward(100)

right(180)
goto(100,100)

setheading(135)
backward(100)

undo()
home()  # Move Turtle back to home position

dot(10)
circle(50)
undo()
circle(50,180)
undo()
circle(50, steps=6)

while True:
    speed(5)
    left(90)

done()  # Inflate canvas