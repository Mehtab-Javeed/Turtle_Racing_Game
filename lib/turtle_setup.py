import turtle

WIDTH = 800
HEIGHT = 600

# Define a list of colors for the turtles
COLOURS = [
    "red", "blue", "green", "orange", "purple",
    "yellow", "cyan", "pink", "brown", "black"
]

# Initialize the turtle screen with the specified width and height


def init_screen(colours):
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game")
    return screen

# Create turtle racers based on the provided colors and position them at the starting line


def create_turtles(colours):
    turtles = []

    start_y = HEIGHT // 2 - 50  # Starting y-coordinate for the first turtle
    spacing = 50  # Vertical spacing between turtles

    for i, colour in enumerate(colours):
        racer = turtle.Turtle()  # Create a new turtle racer
        racer.shape("turtle")
        racer.color(colour)
        racer.penup()
        # Position the turtle at the starting line
        racer.goto(-WIDTH // 2 + 20, start_y - i * spacing)
        racer.pendown()  # Lower the pen to start drawing when

        turtles.append(racer)  # Add the turtle racer to the list of turtles

    return turtles
