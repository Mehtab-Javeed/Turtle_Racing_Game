import turtle

WIDTH = 800
HEIGHT = 600

COLOURS = [
    "red", "blue", "green", "orange", "purple",
    "yellow", "cyan", "pink", "brown", "black"
]


def init_screen(colours):
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game")
    return screen


def create_turtles(colours):
    turtles = []

    start_y = HEIGHT // 2 - 50
    spacing = 50

    for i, colour in enumerate(colours):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(colour)
        racer.penup()
        racer.goto(-WIDTH // 2 + 20, start_y - i * spacing)
        racer.pendown()

        turtles.append(racer)

    return turtles
