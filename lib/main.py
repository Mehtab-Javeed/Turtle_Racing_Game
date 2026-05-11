from racers import get_number_of_racers
import turtle_setup
import random
import turtle

# Main function to run the turtle racing game


def main():
    print("main loaded")

    racers = get_number_of_racers()  # Get the number of racers from the user

    # Shuffle the colors to ensure randomness in turtle colors
    random.shuffle(turtle_setup.COLOURS)
    # Select the first 'racers' colors from the shuffled list
    colours = turtle_setup.COLOURS[:racers]

    screen = turtle_setup.init_screen(colours)  # Initialize the turtle screen
    # Create turtle racers based on the selected colors
    turtles = turtle_setup.create_turtles(colours)

    race = True  # Start the race
    while race:
        for racer in turtles:
            # Move each turtle forward by a random distance between 1 and 10
            distance = random.randint(1, 10)
            racer.forward(distance)

            if racer.xcor() > 350:
                winner_colour = racer.pencolor()  # Get the color of the winning turtle
                print(f"The winner is the {winner_colour} turtle!")
                race = False
                break

    screen.mainloop()  # Keep the turtle graphics window open until the user closes it


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
