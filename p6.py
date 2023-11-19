# Develop a basic racing game where multiple Turtle graphics entities compete. Add user controls to simulate a race.

import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create turtles
turtle_1 = turtle.Turtle()
turtle_1.shape("turtle")
turtle_1.color("red")
turtle_1.penup()
turtle_1.goto(-300, 0)

turtle_2 = turtle.Turtle()
turtle_2.shape("turtle")
turtle_2.color("blue")
turtle_2.penup()
turtle_2.goto(-300, -50)

# Function to move turtle_1
def move_turtle_1():
    y = turtle_1.ycor()
    y += 20
    turtle_1.sety(y)

# Function to move turtle_2
def move_turtle_2():
    y = turtle_2.ycor()
    y += 20
    turtle_2.sety(y)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_turtle_1, "Up")
screen.onkeypress(move_turtle_2, "Down")

# Main game loop
while True:
    # Move the turtles forward
    turtle_1.forward(random.randint(1, 5))
    turtle_2.forward(random.randint(1, 5))

    # Check for the winner
    if turtle_1.xcor() > 300:
        print("Turtle 1 wins!")
        break
    elif turtle_2.xcor() > 300:
        print("Turtle 2 wins!")
        break

turtle.done()
