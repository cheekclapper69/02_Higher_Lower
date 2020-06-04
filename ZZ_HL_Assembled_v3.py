import random


# Number checking function goes here
def int_check(question, low=None, high=None):
    # sets up error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue
            else:
                return response

        except ValueError:
            print(error)


# Main routine

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)

# **** Main Routine *****

# Initialise variables

guesses_allowed = int_check("Max guesses? ")

num_won = 0
rounds_played = 0
secret = random.randint(lowest, highest)
guesses_left = guesses_allowed
already_guessed = ""
guess = ""

# list holds # of guesses used in each game
game_stats = []

# start game

while rounds_played < rounds:
    print()
    print("Round # {}".format(rounds_played + 1))
    secret = random.randrange(lowest, highest)

    guess = ""
    guesses_left = guesses_allowed

    while guess != secret and guesses_left >= 1:

        guess = int(input("Guess: "))

        if guess in already_guessed:
            print("You already guessed that number! Please rty again.  "
                  "you *still* have {} guesses left".format(guesses_left))
            break

    while guess != secret and guesses_left >= 1:
        guess = int_check("Guess: ", lowest, highest)
        guesses_left -= 1

        if guesses_left >= 1:
            if guess < secret:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

            elif guess > secret:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
        else:
            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high")

        if guess == secret:
            if guesses_left == guesses_allowed - 1:
                print("Amazing! You got it in one guess")
                num_won += 1
            else:
                print("Well done, you got it in {} guesses".format(guesses_allowed - guesses_left))
                num_won += 1

    game_stats.append(guesses_allowed - guesses_left)

    print("Won : {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1

# print game outcomes...
print()
print("*** Score for Each Round...***")
list_count = 1
for item in game_stats:

    # indicates if games has been won or lost
    if item > guesses_allowed:
        status = "lost, ran out of guesses"
    else:
        status = "won"

    print("Round {}: {})".format(list_count, item))
    list_count += 1

# Calculate statistics
game_stats.sort()
best = game_stats[0]
worst = game_stats[-1]
average = sum(game_stats) / len(game_stats)

print()
print("*** Summary Statistics ***")
print("Best: {}".format(best))
print("Worst: {}".format(worst))
print("Average: {:.2f}".format(average))

