#Carla Epperson
#October 30,2024
#P4LAB1a
#Square and Triangle


import turtle

# Set up turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(1)

# Draw a square in red
t.color("red")
side = 0
while side < 4:
    t.forward(150)  
    t.right(90)
    side += 1

# Move for the triangle
t.penup()
t.goto(100, -100)   
t.pendown()

# Draw a triangle in purple
t.color("purple")
side = 0
while side < 3:
    t.forward(150)   
    t.left(120)
    side += 1
