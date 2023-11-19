import turtle

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

# Function to draw a circle
def draw_circle(radius):
    turtle.circle(radius)

# Function to draw an equilateral triangle
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Set up Turtle
turtle.speed(2)  # Set the drawing speed (1-10, 1 is the slowest, 10 is the fastest)

# Draw shapes
draw_square(100)
turtle.penup()  # Move to a new position without drawing
turtle.goto(-150, 0)
turtle.pendown()
draw_rectangle(120, 80)
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
draw_circle(50)
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
draw_triangle(100)

# Close the Turtle graphics window when clicked
turtle.done()

