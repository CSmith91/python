import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... try again')
            continue # ensures we don't finish the rest of the conditionals - we go straight back to the top

        if 2 <= racers <= 10:
            return racers
        else:
            print('Please enter a number between 2 and 10')

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 10)
            racer.forward(distance)

            x, y = racer.pos() # this gives us the turtle position on the screen
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)] # we want to get the winning turtle color, which we can obtain through indexing

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors): # enumerate gives the index as well as the value of all the elements in colors
        # i.e. ['red', 'green', 'blue'] would give 0 red, 1 green and 2 blue 
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # set position of racer
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS) # will select unique options each time
colors = COLORS[:racers] # a slice up to the number of racers we have

winner = race(colors)
print("The winner is the turtle with the colour:", winner)
time.sleep(5)