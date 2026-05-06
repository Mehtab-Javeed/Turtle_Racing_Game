import turtle
import main

WIDTH, HEIGHT = 500, 500
COLOURS = ["red", "blue", "green", "yellow", "orange",
           "purple", "pink", "cyan", "magenta", "brown"]


def create_turtle(colours):
    turtles = []  # Create an empty list to store the turtle objects
    for colour in colours:
        racer = turtle.Turtle()  # Create a new turtle object for each colour
        racer.color(colour)
        racer.shape("turtle")
        racer.left(90)  # Rotate the turtle to face upwards
        racer.penup()  # Lift the pen to avoid drawing lines
        racer.setpos()  # Set the turtle's position to the starting line (you can adjust the coordinates as needed)
        racer.pendown()  # Lower the pen to start drawing
        turtles.append(racer)  # Add the turtle object to the list
    # return turtles


def init_turtle(COLOURS):
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")
    racer = turtle.Turtle()
    racer.color(COLOURS)
    racer.shape("turtle")
    racer.penup()
    racer.speed(1)
    racer.moveforward(100)
    racer.moveright(90)
    racer.moveforward(200)
    return racer
