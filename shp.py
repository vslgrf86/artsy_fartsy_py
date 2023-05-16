import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle instance
t = turtle.Turtle()

# Set the turtle's speed to fastest
t.speed(0)

# Define the color palette
colors = ["#FF5733", "#F2C80F", "#007FFF", "#900C3F", "#5A5AAD"]

# Define the number of shapes to draw
num_shapes = 100

# Loop through and draw the shapes
for i in range(num_shapes):
    # Choose a random color
    color = random.choice(colors)

    # Choose a random shape
    shape = random.choice(["circle", "triangle", "square"])

    # Choose a random size for the shape
    size = random.randint(10, 100)

    # Choose a random position for the shape
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    # Set the turtle's color and fill color
    t.color(color)
    t.fillcolor(color)

    # Move the turtle to the correct position
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw the shape
    if shape == "circle":
        t.circle(size)
    elif shape == "triangle":
        for i in range(3):
            t.forward(size)
            t.left(120)
    elif shape == "square":
        for i in range(4):
            t.forward(size)
            t.left(90)

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed
turtle.done()
