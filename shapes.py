import turtle
import random

# Create turtle object and set the speed to the maximum value
t = turtle.Turtle()
t.speed(0)

# Set the window size and background color
turtle.setup(800, 600)
turtle.bgcolor("#000000")

# Set the list of colors
colors = ["#D3839E", "#8C4B7D", "#4A2545", "#E7D8C9", "#F5A962"]

# Define a function to draw a random shape
def draw_shape():
    t.pencolor(random.choice(colors))
    sides = random.randint(3, 12)
    length = random.randint(10, 100)
    t.penup()
    t.goto(random.randint(-turtle.window_width() // 2, turtle.window_width() // 2),
           random.randint(-turtle.window_height() // 2, turtle.window_height() // 2))
    t.pendown()
    for i in range(sides):
        t.forward(length)
        t.right(360 / sides)

# Set the delay to 0.01 seconds
delay = 0.01

# Loop forever
while True:
    draw_shape()
    turtle.update()
    turtle.delay(delay)

turtle.done()
