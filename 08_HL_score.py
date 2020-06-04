SECRET = 7
GUESSES_ALLOWED = 4
rounds = 3


num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >= 1:
        already_guessed = []

        guess = int(input("Guess: "))

        # add guess to list for stats / to prevent duplicates
        already_guessed.append(guess)
        guesses_left -= 1

        # has guesses left
        if guesses_left >= 1:

            if guess < SECRET:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

            elif guess > SECRET:
                print("Too high, try a lower number. Guesses left {}".format(guesses_left))

            else:
                print("Well done")
                round += 1

        # Out of guesses!
        else:
            if guess < SECRET:
                print("Too low!")
            elif guess > SECRET:
                print("Too high!")
            else:
                print("Sorry - you lose this round as you have run out of guesses")

        print("won: {} \t lost: {}".format(num_won, rounds_played - num_won + 1 ))
        rounds_played += 1