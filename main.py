#Turtle party project
by Jacques Duval

import turtle

turtle.color("green")
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(90)

  
polygon(4,100) 
