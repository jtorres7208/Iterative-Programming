# Problem 3
#Julian Torres
#2/18/2024

import turtle

sides = int(input("Enter number of sides: ")) 
length = int(input("Enter length of side: "))
line_color = input("Enter line color: ")
fill_color = input("Enter fill color: ")

turtle.color(line_color)

for i in range(sides):
    turtle.forward(length)
    turtle.right(360/sides)

turtle.fillcolor(fill_color)
turtle.begin_fill()
for i in range(sides):
    turtle.forward(length)
    turtle.right(360/sides)    
turtle.end_fill()
