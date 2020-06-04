SECRET = 7
GUESSES_ALLOWED = 5

guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# start game
while guess != SECRET and guesses_left >= 1:
    already_guessed = []

    guess = int(input("Guess: "))

    # add guess to list for stats / to prevent duplicates
    already_guessed.append(guess)
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
        print("well done, you got it in {} guesses".format(len(already_guessed)))
    num_won += 1
else:
    print("Sorry - you lose this round as you have run out of guesses")