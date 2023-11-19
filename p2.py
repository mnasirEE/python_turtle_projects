import turtle

def draw_initials(name):
    # Create a Turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a Turtle object
    my_turtle = turtle.Turtle()
    my_turtle.speed(2)  # Set turtle speed (1-10, 1 being the slowest, 10 being the fastest)

    # Move the turtle to starting position
    my_turtle.penup()
    my_turtle.goto(-100, 0)
    my_turtle.pendown()

    # Draw initials based on the first two characters of the name
    initials = name[:2].upper()

    for initial in initials:
        if initial == 'A':
            my_turtle.backward(30)
            my_turtle.left(60)
            my_turtle.forward(60)
            my_turtle.backward(30)
            my_turtle.right(120)
        elif initial == 'B':
            my_turtle.forward(60)
            my_turtle.right(90)
            my_turtle.circle(-30, 180)
            my_turtle.right(180)
            my_turtle.circle(-30, 180)
            my_turtle.right(90)
            my_turtle.forward(60)
            my_turtle.penup()
            my_turtle.forward(15)  # Space between initials
            my_turtle.pendown()
        else:
            # Add more conditions for other initials as needed
            pass

    # Close the Turtle graphics window on click
    screen.exitonclick()

# Get user input for the name
user_name = input("Enter your name: ")

# Call the function to draw initials
draw_initials(user_name)
