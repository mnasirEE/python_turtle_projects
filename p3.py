""" Implement a spirograph drawing program using Turtle.
 Allow users to customize parameters like the number of circles 
 and rotation angles. """

import turtle
import math

# Function to draw a spirograph
def draw_spirograph(circles, angle):
    turtle.speed(0)  # Set the drawing speed (0 is the fastest)

    for _ in range(circles):
        turtle.circle(100)
        turtle.left(angle)

    turtle.hideturtle()

# Get user input for the number of circles and rotation angle
num_circles = int(input("Enter the number of circles: "))
rotation_angle = int(input("Enter the rotation angle in degrees: "))

# Draw the spirograph
draw_spirograph(num_circles, rotation_angle)

# Keep the window open
turtle.done()
