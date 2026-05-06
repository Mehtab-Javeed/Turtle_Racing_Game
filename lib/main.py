from racers import get_number_of_racers
import turtle_setup
import random


racers = get_number_of_racers()
print(f"Number of racers: {racers}")

turtle_setup.init_turtle(turtle_setup.COLOURS)
random.shuffle(turtle_setup.COLOURS)
colours = turtle_setup.COLOURS[:racers]
print(f"Racers' colours: {colours}")
