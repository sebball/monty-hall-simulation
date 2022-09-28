import random

NUM_SIMULATIONS = int(input("How many simulations of the Monty Hall problem do you want to run?"))

# Loop over the simulation a certain amount of times
counter = 0
wins_staying = []
wins_changing = []

while counter < NUM_SIMULATIONS:
    # Create list of length 3 representing the doors, with true representing a prize and false a goat
    doors = []
    winning_door = random.randint(0, 2)

    for i in range(3):
        if i == winning_door:
            doors.append(True)
        else:
            doors.append(False)
    # First guess of contestant
    first_guess = random.randint(0, 2)

    # Simulate the host revealing a goat by removing one False from list
    for i in range(3):
        # Don't reveal goat if door has been guessed
        if i == first_guess:
            continue
        # Don't reveal goat if it is actually prize
        elif doors[i]:
            continue
        # Else reveal goat
        else:
            del doors[i]
            # Entries in doors list indexed higher than i will change to one index lower due to "revealing" the goat
            # Therefore if first_guess is greater than i, reduce it by one.
            if first_guess > i:
                first_guess -= 1
            break

        # Record results for what happens if guest does not change guess
    if doors[first_guess]:
        wins_staying.append(True)
    else:
        wins_staying.append(False)

    # Make second guess one if first is zero, and zero if first is one to simulate changing guess
    if first_guess == 0:
        second_guess = 1
    elif first_guess == 1:
        second_guess = 0

    if doors[second_guess]:
        wins_changing.append(True)
    else:
        wins_changing.append(False)

    counter += 1

staying_percent = round((sum(wins_staying) / NUM_SIMULATIONS) * 100, 2)
changing_percent = round((sum(wins_changing) / NUM_SIMULATIONS) * 100, 2)

print(f"When staying with the first guess there were {sum(wins_staying)} wins out of {NUM_SIMULATIONS} simulations\n"
      f"{staying_percent}%\n")

print(f"When changing the guess there were {sum(wins_changing)} wins out of {NUM_SIMULATIONS} simulations\n"
      f"{changing_percent}%\n")









