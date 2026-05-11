def get_number_of_racers():
    while True:
        try:
            # Prompt the user to enter the number of racers
            racers = int(input("Enter the number of racers (2-10): "))

            if 2 <= racers <= 10:
                return racers
            else:
                print("Invalid input. Please enter a number between 2 and 10.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
