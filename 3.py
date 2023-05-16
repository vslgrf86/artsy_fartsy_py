import time
import turtle
import random
import ctypes

# Get the width and height of the screen
user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def good_sleep(t):
     start_time = time.time()
     while time.time() < start_time + 1:
        turtle.update()
        time.sleep(.1)


# Create turtle object and set the speed to the maximum value
t = turtle.Turtle()
t.speed(0)

# Set the window size and background color
turtle.setup(screen_width, screen_height)
turtle.bgcolor("#000000")

# Set the list of colors
colors = ["#8A2BE2", "#6495ED", "#00CED1", "#228B22", "#FFD700", "#FFA500", "#FF6347", "#FF69B4"]

# list of words related to the short story. w/stopwords is only the first paragraph to date

words = ['man', 'grew', 'small', 'country', 'fighting', 'crohn', 'disease', 'since', 'adolescence', 'despite']

# Create a set to store unique words
# unique_words = set()
unique_words = list(set(words))

# Set the delay to 0.00 seconds
delay = 0

# Hide the turtle cursor
turtle.hideturtle()

# Loop until all words have been written to the screen
while unique_words:

    try:

        # Choose a random word that has not already been written
        word = random.choice(unique_words)
        unique_words.remove(word)

        # Write the word and add it to the set of unique words

        x = random.randint(-turtle.window_width() // 0.65, turtle.window_width() // 0.65)
        y = random.randint(-turtle.window_height() // 0.65, turtle.window_height() // 0.65)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor(random.choice(colors))
        font_size = random.randint(10, 115)
        t.write(word, align="center", font=("Garamond", font_size, "bold"))
        turtle.update()
        turtle.delay(delay)

        if not unique_words:
            turtle.showturtle()

            good_sleep(5)

            turtle.clearscreen()
            turtle.bgcolor("#000000")
            good_sleep(1)

            turtle.reset()
            turtle.bgcolor("#000000")
            turtle.update()
            unique_words = list(set(words))

    except turtle.Terminator:
        break
