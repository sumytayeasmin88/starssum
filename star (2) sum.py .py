from turtle import *
from random import randint

# Page setup 
setup(800, 500)
speed(0)
bgcolor("navy blue")

# Function to draw one star
def star():
    color("yellow")
    begin_fill()
    for i in range(15):
        forward(10)
        right(144)
    end_fill()

# Draw multiple stars at random locations on the screen
for i in range(50):
    x = randint(-500, 500)
    y = randint(-350, 350)
    star()
    penup()
    goto(x, y)
    pendown()

# Moon - Part 1
penup()
goto(-300, 100)
pendown()
color("white")
begin_fill()
circle(60)
end_fill()

# Moon - Part 2
penup()
goto(-280, 100)
pendown()
color("navy blue")
begin_fill()
circle(60)
end_fill()

hideturtle()
