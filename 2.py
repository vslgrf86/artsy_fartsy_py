import time
import turtle
import random


def good_sleep(t):
     start_time = time.time()
     while time.time() < start_time + 1:
        turtle.update()
        time.sleep(.1)


# Create turtle object and set the speed to the maximum value
t = turtle.Turtle()
t.speed(0)

# Set the window size and background color
turtle.setup(800, 600)
# set bg for the first loop
turtle.bgcolor("#000000")


# Set the list of colors
colors = ["#8A2BE2", "#6495ED", "#00CED1", "#228B22", "#FFD700", "#FFA500", "#FF6347", "#FF69B4"]

# list of words related to the short story. w/stopwords is only the first paragraph to date

words = ['man', 'grew', 'small', 'country', 'fighting', 'crohn', 'disease', 'since', 'adolescence', 'despite', 'struggles', 'bright', 'young', 'man',
'determined', 'make', 'life', 'always', 'wanted', 'go', 'london', 'oddly', 'liked', 'weather', 'london', 'lost', 'beloved', 'dog', 'parents', 'leaving',
'felt', 'suffocating', 'living', 'house', 'grew', 'left', 'empty', 'wanted', 'leave', 'asking', 'left', 'leave', 'least', 'make', 'something', 'said', 'left',
'homeland', 'late', 'decided', 'venture', 'unknown', 'escape', 'grow', 'turn', 'pain', 'something', 'positive', 'heal', 'stepped', 'plane', 'heavy', 'heart', 'still',
'sure', 'everything', 'wanted', 'leave', 'everything', 'behind', 'went', 'another', 'country', 'arrived', 'new', 'country', 'nothing', 'clothes', 'back', 'bit',
'cash', 'name', 'bit', 'fear', 'whole', 'lot', 'grit', 'life', 'anything', 'easy', 'beginning', 'worked', 'fingers', 'bone', 'taking', 'odd', 'job', 'could',
'find', 'hope', 'better', 'life', 'also', 'lived', 'small', 'dingy', 'apartment', 'little', 'mattress', 'floor', 'years', 'new', 'country', 'started', 'study',
'economics', 'university', 'early', 'first', 'time', 'long', 'time', 'felt', 'like', 'something', 'mattered', 'something', 'liked', 'chance', 'study', 'back',
'home', 'also', 'another', 'person', 'back', 'interest', 'studying', 'seemed', 'early', 'years', 'transformational', 'bit', 'contradictory', 'old', 'life', 'turning',
'point', 'started', 'building', 'career', 'clawed', 'way', 'landed', 'good', 'job', 'kept', 'climbing', 'achieved', 'ever', 'thought', 'possible', 'friends', 'back',
'home', 'envying', 'also', 'gained', 'respect', 'among', 'old', 'peers', 'social', 'adjustment', 'changed', 'found', 'longer', 'fit', 'changed', 'grown', 'matured',
'become', 'independent', 'old', 'self', 'distant', 'memory', 'man', 'used', 'pushover', 'always', 'eager', 'please', 'always', 'knew', 'past', 'would', 'come', 'back',
'haunt', 'one', 'day', 'social', 'expectation', 'fall', 'line', 'old', 'traditions', 'women', 'rejected', 'threw', 'feet', 'wanting', 'success', 'found', 'could', 'connect',
'either', 'time', 'hit', 'late', 'thirties', 'make', 'choice', 'stick', 'dreams', 'go', 'back', 'old', 'life', 'love', 'triangle', 'two', 'women', 'back', 'home', 'adding',
'weight', 'already', 'heavy', 'load', 'make', 'things', 'worse', 'embroiled', 'bitter', 'legal', 'battle', 'sister', 'family', 'property', 'pressure', 'crushing', 'drowning',
'suffocating', 'career', 'taking', 'rest', 'life', 'miserable', 'wreck', 'new', 'old', 'country', 'know', 'way', 'cost', 'returning', 'would', 'heavy', 'would', 'give', 'career',
'aspirations', 'felt', 'connection', 'old', 'places', 'faces', 'cost', 'staying', 'would', 'equally', 'heavy', 'struggling', 'loneliness', 'depression', 'questioned', 'life',
'identity', 'sense', 'belonging', 'meant', 'live', 'free', 'spirit', 'drifting', 'aimlessly', 'world', 'always', 'prided', 'independence', 'ability', 'stand', 'two', 'feet',
'realised', 'lost', 'alone', 'ever', 'know', 'belonged', 'belonged', 'anywhere', 'confronted', 'biggest', 'dilemma', 'life', 'could', 'keep', 'living', 'like', 'torn', 'two',
'worlds', 'forever', 'know', 'make', 'choice', 'know', 'path', 'take', 'knew', 'make', 'decision', 'afraid', 'would', 'regret', 'either', 'way', 'give', 'everything', 'built',
'go', 'back', 'familiar', 'comforts', 'old', 'life', 'stay', 'try', 'find', 'way', 'fill', 'void', 'soul', 'would', 'ever', 'truly', 'feel', 'home', 'home', 'place', 'feeling',
'comfort', 'familiarity', 'man', 'felt', 'lost', 'alone', 'clear', 'path', 'forward', 'like', 'long', 'time', 'lost', 'thought', 'unable', 'make', 'decision', 'knew', 'life',
'ongoing', 'battle', 'whatever', 'chose', 'decision', 'would', 'biggest', 'one', 'thought', 'way', 'maybe', 'way', 'find', 'place', 'world', 'way', 'reconcile', 'past', 'present',
'future', 'make', 'work', 'make', 'peace', 'accept', 'flaws', 'learn', 'forgive', 'others', 'mistakes', 'made', 'things', 'could', 'change', 'let', 'go', 'past', 'embrace', 'present',
'know', 'future', 'held', 'knew', 'make', 'amends', 'keep', 'moving', 'forward', 'keep', 'searching', 'place', 'world', 'keep', 'living', 'facing', 'trauma', 'demons', 'know', 'ready',
'kept', 'muted', 'long', 'time', 'pretending', 'exist', 'universe', 'one', 'moment', 'telling', 'screwed', 'everything', 'next', 'everything', 'going', 'alright']

# Create a set to store unique words
# unique_words = set()
unique_words = list(set(words))

# Set the delay to 0.00 seconds
delay = 10

# Hide the turtle cursor
turtle.hideturtle()

# Loop until all words have been written to the screen
while unique_words:

    try:

        # Choose a random word that has not already been written
        word = random.choice(unique_words)
        unique_words.remove(word)

        # Write the word and add it to the set of unique words

        x = random.randint(-turtle.window_width() // 0.75, turtle.window_width() // 0.75)
        y = random.randint(-turtle.window_height() // 0.75, turtle.window_height() // 0.75)
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

            good_sleep(0)

            turtle.clearscreen()
            # set bg for the transition
            turtle.bgcolor("#000000")
            good_sleep(0)

            turtle.reset()
            # set bg for every loop
            turtle.bgcolor("#000000")
            turtle.update()
            unique_words = list(set(words))

    except turtle.Terminator:
        break