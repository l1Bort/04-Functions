# draw_figures.py

import turtle
import figures     

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Use the pen created above
turtle.Turtle._screen = window
turtle.Turtle._pen = pen

# Draw a square with length 100
figures.draw_square(100)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
