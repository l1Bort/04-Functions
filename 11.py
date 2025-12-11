###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#

import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

# Square 1
pen.penup()
pen.goto(-150, 150)
pen.pendown()
figures.draw_square(pen, 80)

# Square 2
pen.penup()
pen.goto(100, 150)
pen.pendown()
figures.draw_square(pen, 80)

# Triangle 1
pen.penup()
pen.goto(-150, -75)
pen.pendown()
figures.draw_triangle(pen, 100)

# Triangle 2
pen.penup()
pen.goto(100, -75)
pen.pendown()
figures.draw_triangle(pen, 100)

# Rectangle 1
pen.penup()
pen.goto(-150, -150)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)

# Rectangle 2
pen.penup()
pen.goto(100, -150)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)

pen.hideturtle()
window.mainloop()
