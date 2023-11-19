#  Build a program to draw a fractal tree using Turtle graphics. Allow users to control the depth and angle of the branches.


import turtle

def draw_fractal_tree(branch_length, t, angle, depth):
    if depth == 0:
        return
    else:
        t.forward(branch_length)
        t.left(angle)
        draw_fractal_tree(branch_length * 0.7, t, angle, depth - 1)
        t.right(2 * angle)
        draw_fractal_tree(branch_length * 0.7, t, angle, depth - 1)
        t.left(angle)
        t.backward(branch_length)

def main():
    # Set up Turtle
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(2)
    t.color("green")

    # Get user input for depth and angle
    depth = int(turtle.numinput("Fractal Tree", "Enter the depth of the tree:", default=4, minval=1))
    angle = int(turtle.numinput("Fractal Tree", "Enter the angle between branches:", default=30, minval=1))

    # Position the turtle
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    # Draw the fractal tree
    draw_fractal_tree(100, t, angle, depth)

    # Close the window on click
    screen.exitonclick()

if __name__ == "__main__":
    main()
