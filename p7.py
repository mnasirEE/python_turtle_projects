# Extend Turtle graphics to create a 3D environment. Implement basic 3D shapes and allow users to navigate in the space.


import turtle
import math


# Set up the turtle screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("3D Turtle Graphics")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Define a function to draw a 3D cube
def draw_3d_cube(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.goto(t.xcor() - size // 2, t.ycor() - size // 2, t.zcor() - size // 2)
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.goto(t.xcor() + size // 2, t.ycor() + size // 2, t.zcor() - size // 2)
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.goto(t.xcor() - size // 2, t.ycor() + size // 2, t.zcor() - size // 2)
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Set initial position and orientation
t.penup()
t.setpos(0, 0)
t.setheading(90)
t.pendown()

# Set the size of the 3D cube
cube_size = 100

# Main loop to navigate in the 3D space
while True:
    # Get user input for navigation
    action = wn.textinput("Navigation", "Move (WASD), Quit (Q):")
    
    if action == 'q' or action == 'Q':
        break

    # Move forward
    elif action == 'w' or action == 'W':
        t.forward(20)

    # Move backward
    elif action == 's' or action == 'S':
        t.backward(20)

    # Strafe left
    elif action == 'a' or action == 'A':
        t.left(90)
        t.forward(20)
        t.right(90)

    # Strafe right
    elif action == 'd' or action == 'D':
        t.right(90)
        t.forward(20)
        t.left(90)

    # Clear the screen and redraw the 3D cube
    t.clear()
    draw_3d_cube(cube_size)
turtle.done()
# Close the turtle graphics window when done
# wn.bye()
