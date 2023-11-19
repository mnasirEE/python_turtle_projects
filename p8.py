# Build a physics simulation using Turtle. Simulate basic physical laws like gravity, friction, and collisions with Turtle graphics.

import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Physics Simulation with Turtle")
screen.bgcolor("white")
screen.setup(width=600, height=400)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.speed(0)
ball.goto(0, 200)

# Set initial velocity
ball.dx = 2
ball.dy = -2

# Gravity and friction coefficients
gravity = 0.1
friction = 0.98

# Main game loop
while True:
    # Update ball position
    ball.dy -= gravity
    ball.dy *= friction
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Bounce off the walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    # Bounce off the floor
    if ball.ycor() < -190:
        ball.sety(-190)
        ball.dy *= -1

    # Update the display
    screen.update()

    # Pause for a short time
    time.sleep(0.01)

