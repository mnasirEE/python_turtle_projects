# Create a Turtle program that generates a simple maze and uses an algorithm (like depth-first search) to solve it.

import turtle
import random

# Constants
CELL_SIZE = 20
MAZE_SIZE = 15

# Maze grid
maze = [[0] * MAZE_SIZE for _ in range(MAZE_SIZE)]

# Turtle setup
screen = turtle.Screen()
screen.title("Maze Generator and Solver")
screen.bgcolor("white")
screen.setup(width=MAZE_SIZE * CELL_SIZE + 20, height=MAZE_SIZE * CELL_SIZE + 20)
screen.tracer(0)

turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-MAZE_SIZE * CELL_SIZE // 2, MAZE_SIZE * CELL_SIZE // 2)

# Maze generation using depth-first search
def generate_maze(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + 2 * dx, y + 2 * dy
        if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE and maze[ny][nx] == 0:
            maze[y + dy][x + dx] = 1
            maze[ny][nx] = 1
            generate_maze(nx, ny)


def draw_maze():
    for y in range(MAZE_SIZE):
        for x in range(MAZE_SIZE):
            if maze[y][x] == 1:
                turtle.goto(x * CELL_SIZE - MAZE_SIZE * CELL_SIZE // 2, MAZE_SIZE * CELL_SIZE // 2 - y * CELL_SIZE)
                turtle.pendown()
                turtle.setheading(0)
                turtle.forward(CELL_SIZE)
                turtle.right(90)
                turtle.forward(CELL_SIZE)
                turtle.right(90)
                turtle.forward(CELL_SIZE)
                turtle.right(90)
                turtle.forward(CELL_SIZE)
                turtle.penup()


# Maze solving using depth-first search
def solve_maze(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE and maze[y][x] == 0:
        maze[y][x] = 2  # Mark the path

        if x == MAZE_SIZE - 1 and y == MAZE_SIZE - 1:
            return True  # Reached the exit

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            if solve_maze(x + dx, y + dy):
                return True

        maze[y][x] = 3  # Mark as visited (dead end)

    return False


# Draw the maze
generate_maze(0, 0)
draw_maze()

# Solve the maze
maze_solved = solve_maze(0, 0)

# Draw the solution path
if maze_solved:
    turtle.color("red")
    turtle.width(3)

    for y in range(MAZE_SIZE):
        for x in range(MAZE_SIZE):
            if maze[y][x] == 2:
                turtle.goto(x * CELL_SIZE - MAZE_SIZE * CELL_SIZE // 2 + CELL_SIZE // 2,
                            MAZE_SIZE * CELL_SIZE // 2 - y * CELL_SIZE - CELL_SIZE // 2)
                turtle.pendown()
                turtle.dot(CELL_SIZE - 2)
                turtle.penup()

# Display the result
turtle.done()

