# Create an interactive game using Turtle graphics. This could be a maze-solving game, a puzzle, or a platformer with Turtle entities.

import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Maze Solver")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# Create the maze
maze = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X                  X",
    "X XXXXXXXXXXXXXX X X",
    "X XS           X X X",
    "X XXXXXXXXXX X X X X",
    "X XXXXXXXXXX X X X X",
    "X XXXXXXXXXX X X X X",
    "X XXXXXXXXXX X X X X",
    "X XXXX       X X X X",
    "X XXXX XXXXXXXXX X X",
    "X XXXX XXXXXXXXX X X",
    "X     XXXXXXXXX X X",
    "X XXX XXXXXXXXX X X",
    "X XXX         X X X",
    "X XXXXXXXXXXX X X X",
    "X             X X X",
    "XXXXXXXXXXXXXXX X X",
    "XG              X X",
    "XXXXXXXXXXXXXXXXXXXX"
]

# Set up colors
wn.register_shape("animated_circle.gif")
wn.register_shape("animated_circle.gif")
wn.addshape("animated_circle.gif")
wn.addshape("animated_circle.gif")

# Create the maze turtle
maze_turtle = turtle.Turtle()
maze_turtle.shape("square")
maze_turtle.color("black")
maze_turtle.penup()
maze_turtle.speed(0)

# Create the player turtle
player = turtle.Turtle()
player.shape("animated_circle.gif")
player.color("blue")
player.penup()
player.speed(0)

# Initialize the maze
def setup_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            char = maze[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if char == "X":
                maze_turtle.goto(screen_x, screen_y)
                maze_turtle.stamp()
            elif char == "S":
                player.goto(screen_x, screen_y)
            elif char == "G":
                wn.register_shape("animated_circle.gif")
                finish_turtle = turtle.Turtle()
                finish_turtle.shape("animated_circle.gif")
                finish_turtle.color("green")
                finish_turtle.penup()
                finish_turtle.goto(screen_x, screen_y)

# Keyboard bindings
wn.listen()
wn.onkey(lambda: player.setheading(90), "Up")
wn.onkey(lambda: player.setheading(180), "Left")
wn.onkey(lambda: player.setheading(0), "Right")
wn.onkey(lambda: player.setheading(270), "Down")

# Function to check for collision with maze walls
# Function to check for collision with maze walls
def is_collision(x, y):
    maze_row = int((y + 288) // 24)
    maze_col = int((x + 288) // 24)

    # Ensure indices are within bounds
    if 0 <= maze_row < len(maze) and 0 <= maze_col < len(maze[0]):
        return maze[maze_row][maze_col] == "X"
    else:
        return False


# Function to check if the player has reached the goal
def is_goal(x, y):
    maze_row = int((y + 288) // 24)
    maze_col = int((x + 288) // 24)

    # Ensure indices are within bounds
    if 0 <= maze_row < len(maze) and 0 <= maze_col < len(maze[0]):
        return maze[maze_row][maze_col] == "G"
    else:
        return False

# Set up the maze
setup_maze()

# Main game loop
while True:
    wn.update()

    # Move the player forward
    player.forward(2)

    # Check for collisions
    if is_collision(player.xcor(), player.ycor()):
        player.goto(-288, 288)  # Reset to starting position if there is a collision

    # Check for reaching the goal
    if is_goal(player.xcor(), player.ycor()):
        player.goto(-288, 288)
        print("Congratulations! You reached the goal!")
turtle.done()    


