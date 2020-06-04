import random


# number check function
def intcheck(question, low=None, high=None):

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
            
# main routine

lowest = intcheck("Low number: ")
highest = intcheck("High Number: ", lowest + 1)
rounds = intcheck("Rounds:", 1)


secret = random.randint(lowest, highest)
print("spoiler alert", secret)
GUESSES_ALLOWED = random.randint

guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# start game
already_guessed = []

while guess != intcheck("Guess:", lowest, highest)

        # add guess to list for stats / to prevent duplicates
        while guess != secret and guesses_left >= 1:

            if guess in already_guessed:
                print("You already guessed that number! Please rty again.  "
                      "you *still* have {} guesses left".format(guesses_left))
                break

            guesses_left -= 1
            already_guessed.append(guess)

            if guesses_left >= 1:

                if guess < secret:
                    print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

                elif guess > secret:
                    print("Too high, try a lower number. Guesses left {}".format(guesses_left))

            else:
                if guess < secret:
                    print("Too low!")
                elif guess > secret:
                    print("Too high!")

            if guess == secret:

                if guesses_left == GUESSES_ALLOWED - 1:
                    print("Amazing! You got it in one guess")
                else:
                    print("well done, you got it in {} guesses".format(len(already_guessed)))
                num_won += 1
            else:
                print("Sorry - you lose this round as you have run out of guesses")



