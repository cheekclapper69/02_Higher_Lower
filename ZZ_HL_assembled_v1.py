import random


#  Functions go here...
def int_check(question, low=None, high=None):

    # Error messages...
    if low is not None and high is not None:
            error = "please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "please enter an integer that is less than or " \

    else:
        error = "please enter an integer"

    # Check that number is valid...
    while True:

        try:
            response = int(input(question))

            if low is not None and response < low:
                print(error)
                continue

            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

                already_guessed = []
                guesses_left = GUESSES_ALLOWED
                num_won = 0

                guess = ""

                # start game
                while guess != SECRET and guesses_left >= 1:

                    guess = int(input("Guess: "))

                    if guess in already_guessed:
                        print("You already guessed that number! Please rty again.  "
                              "you *still* have {} guesses left".format(guesses_left))
                        continue

                    guesses_left -= 1
                    already_guessed.append(guess)

                    if guesses_left >= 1:

                        if guess < SECRET:
                            print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

                        elif guess > SECRET:
                    else:
                        if guess < SECRET:
                            print("Too low!")
                        elif guess > SECRET:
                            print("Too high!")


# main routine

lowest = int_check("Low number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds:", 1)

SECRET = 10.5
GUESSES_ALLOWED = 5

guesses_left = GUESSES_ALLOWED
num_won = 0
rounds_played = 0

game_stats = []
# start game

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >= 1:
            guess = int_check("guess: ", lowest, highest)
            guesses_left -= 1


        if guesses_left >= 1:
            if guess < SECRET:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

            elif guess > SECRET:
                print("Too high, try a lower number. Guesses left {}".format(guesses_left))

        else:
            if guess < SECRET:
                print("Too low!")
            elif guess > SECRET:
                print("Too high!")

        if guess == SECRET:
            if guesses_left == GUESSES_ALLOWED - 1:
                print("Amazing! You got it in one guess")
            else:
                print("well done, you got it in {} guesses".format(GUESSES_ALLOWED - guesses_left))
            num_won += 1
        else:
            print("Sorry - you lose this round as you have run out of guesses")

    game_stats.append(GUESSES_ALLOWED - guesses_left)

    print("won: {} \t lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1

print("*** Score for each round...***")
list_count = 1
for item in game_stats:

    if item > GUESSES_ALLOWED:
        status = "lost, ran out of guesses"
    else:
        status = "won"

    print("round {}: {})".format(list_count, item))
    list_count +=1

# calculate statistics
game_stats.sort()
best = game_stats.sort[0]
worst = game_stats.sort[-1]
average = sum(game_stats)/len(game_stats)

print()
print("*** summary statistics ***")
print("best: {}".format(best))
print("worst {}".format(worst))
print("average {:.2f}".format(average))
