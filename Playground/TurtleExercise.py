from turtle import *

color('black', 'red')
width(5)
begin_fill()
speed(10)
for _ in range(8):
    forward(50)
    dot()
    left(45)
end_fill()

done()