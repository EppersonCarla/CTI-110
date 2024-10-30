#Carla Epperson
#October 30,2024
#P4LAB1b
#Draw My Initials with turtle


import turtle as t

t.pensize(5)
t.color("blue")

def draw_C():
    t.penup()               
    t.goto(-80, 0)          
    t.pendown()     
    t.setheading(180)         
    t.circle(100, 180)

def draw_E():
    t.penup()               
    t.goto(-40, 0)         
    t.pendown()          
    t.forward(100)            
    t.backward(100)                            
    t.right(90)               
    t.forward(100)          
    t.left(90)
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

draw_C()
draw_E()

t.hideturtle()
t.done()
