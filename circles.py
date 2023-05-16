import turtle
import random

# Set up turtle screen
turtle.setup(800, 800)
turtle.bgcolor('black')

# Define list of colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Set up turtle parameters
turtle.pensize(3)
turtle.speed(0)
turtle.hideturtle()

# Loop through drawing circles at random positions with random colors
for i in range(1000):
    # Randomly select color and position
    color = random.choice(colors)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    radius = random.randint(10, 200)
    
    # Set pen color and position
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    
    # Draw circle
    turtle.circle(radius)

# Exit on click
turtle.exitonclick()
