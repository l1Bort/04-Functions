###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Draw square
pen.penup()
pen.goto(-150, 150)
pen.pendown()
figures.draw_square(80)

pen.penup()
pen.goto(100, 150)
pen.pendown()
figures.draw_square(80)

# Draw triangle
pen.penup()
pen.goto(-150, 0)
pen.pendown()
figures.draw_triangle(100)

pen.penup()
pen.goto(100, 0)
pen.pendown()
figures.draw_triangle(100)

# Draw rectangle
pen.penup()
pen.goto(-150, -150)
pen.pendown()
figures.draw_rectangle(120, 60)

pen.penup()
pen.goto(100, -150)
pen.pendown()
figures.draw_rectangle(120, 60)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
