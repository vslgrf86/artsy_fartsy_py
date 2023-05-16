import turtle
import random

# Create turtle object and set the speed to the maximum value
t = turtle.Turtle()
t.speed(0)

# Set the window size and background color
turtle.setup(600, 1200)
turtle.bgcolor("#000000")

# Set the list of colors
colors = ["#C18D6D", "#C9B15E", "#39412F", "#4A6053", "#F9BD47", "#607D5C", "#B6939E", "#C79DA5", "#644B2A", "#CE3825"]

# Set the list of words related to the French Revolution
words =  ['Όταν στις τόσες μου τύχει',
'παιδί που δε μοιάζει στα αλλά',
'Αλλάζω ψυχή',
'και γυαλίζουν τα μάτια μου',
'χαζογελάω',
'και κάνω τρελά όπως κανείς και εσύ',
'Κι αν ξυπόλητη χορεύω, με σημαία μου μια φούστα',
'είναι γιατί σε λατρεύω, και σου κάνω όλα τα γούστα.',
'Κι αν ξυπόλητη χορεύω, με σημαία μιαν αγάπη',
'κάντε άκρη, κάντε άκρη.',
'Θα ‘ρθει κι ο ερωτάς',
'να με τρελάνει',
'τις μέρες με ντύνει',
'τις νύχτες γυμνή με αλλάζει',
'κολλάω και παραμιλάω',
'απρόβλεπτη γίνομαι όπως και εσύ',
'Και αν ξυπόλητη χορεύω, με σημαία μου μια φούστα',
'είναι γιατί σε λατρεύω, και σου κάνω όλα τα γούστα.',
'Κι αν ξυπόλητη χορεύω, με σημαία μιαν αγάπη',
'κάντε άκρη, κάντε άκρη',
'Και αν ξυπόλητη χορεύω, με σημαία μου μια φούστα',
'είναι γιατί σε λατρεύω, και σου κάνω όλα τα γούστα.',
'Και αν ξυπόλητη χορεύω, με σημαία μιαν αγάπη',
'κάντε άκρη']

# Define a function to draw a random shape
def draw_shape():
    t.pencolor(random.choice(colors))
    t.fillcolor(random.choice(colors))
    sides = random.randint(3, 12)
    length = random.randint(10, 100)
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.right(360 / sides)
    t.end_fill()

# Define a function to write a random word in a matching color
def write_word():
    t.penup()
    t.goto(random.randint(-turtle.window_width()//2, turtle.window_width()//2), 
           random.randint(-turtle.window_height()//2, turtle.window_height()//2))
    t.pencolor(random.choice(colors))
    t.write(random.choice(words), align="center", font=("Arial", random.randint(200, 200), "bold"))

# Set the delay to 0.01 seconds
delay = 20

# Loop forever
while True:
    draw_shape()
    write_word()
    turtle.update()
    turtle.delay(delay)

turtle.done()
