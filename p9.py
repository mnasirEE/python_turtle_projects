# Develop a program that generates complex and aesthetically pleasing patterns or artworks using Turtle graphics. This could involve mathematical functions or algorithms.

import turtle
import math
import colorsys

# Function to draw a spirograph pattern
def draw_spirograph(turtle, color, radius):
    turtle.color(color)
    turtle.circle(radius)
    turtle.right(10)

# Set up Turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spirograph Art")

artist = turtle.Turtle()
artist.speed(0)  # Set the maximum drawing speed

# Create a spirograph pattern
for _ in range(36):  # Draw 36 circles to form the pattern
    # Generate a dynamic color using HSV color space
    hue = math.sin(math.radians(artist.heading())) * 0.5 + 0.5
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    color = (color[0], color[1], color[2])

    # Draw the spirograph pattern
    draw_spirograph(artist, color, 100)

# Hide the turtle and display the result
artist.hideturtle()
screen.mainloop()

