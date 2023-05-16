import turtle
import random

# Create turtle object and set the speed to the maximum value
t = turtle.Turtle()
t.speed(0)

# Set the window size and background color
turtle.setup(800, 600)
turtle.bgcolor("#000000")

# Set the list of colors
colors = ["#8A2BE2", "#6495ED", "#00CED1", "#228B22", "#FFD700", "#FFA500", "#FF6347", "#FF69B4"]

# list of words related to the short story. w/stopwords is only the first paragraph to date
words = ["man", "who", "grew", "up", "small", "country", "fighting", "Crohn’s", "disease", "since", 
"adolescence", "Despite", "struggles", "bright", "young", "man", "determined", "make", "most", "life",
 "always", "wanted", "go", "London", "Oddly", "liked", "weather", "London", "lost", "beloved", "dog", 
 "parents", "during", "20s", "leaving", "grief-stricken", "felt", "suffocating", "living", "same", 
 "house", "where", "grew", "up", "but", "now", "left", "empty", "wanted", "leave", "but", "asking", 
 "why?", "left", "now", "nothing", "If", "leave", "least", "can", "make", "something", "said", "left", 
 "home", "late", "20s", "decided", "venture", "unknown", "escape", "grow", "turn", "pain", "something", "positive", "heal"]

# Define a function to draw a random shape with lines
#def draw_shape():
 #   t.pencolor(random.choice(colors))
  #  t.fillcolor("white")
   # t.begin_fill()
    #sides = random.randint(3, 12)
    #length = random.randint(50, 150)
    #angle = 360 / sides
    #for i in range(sides):
     #   t.forward(length)
      #  t.right(angle)
       # t.pendown()
        #t.forward(length / 2)
        #t.penup()
        #t.backward(length / 2)
        #t.left(angle)
   # t.end_fill()

# Set the delay to 0.01 seconds
delay = 0.01

# Loop forever
while True:
    x = random.randint(-turtle.window_width() // 2, turtle.window_width() // 2)
    y = random.randint(-turtle.window_height() // 2, turtle.window_height() // 2)
    t.penup()
    t.goto(x, y)
    t.pendown()
    #draw_shape()
    t.penup()
    x += random.randint(-100, 100)
    y += random.randint(-100, 100)
    t.goto(x, y)
    t.pencolor(random.choice(colors))
    t.write(random.choice(words), align="center", font=("Arial", 20, "bold"))
    turtle.update()
    turtle.delay(delay)

turtle.done()
