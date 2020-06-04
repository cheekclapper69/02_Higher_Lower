# HL component 3 _ compares user guess

SECRET = 7

guess = ""

while guess != SECRET:

    guess = int(input("guess: "))

    if guess < SECRET:
        print("Too high, try a lower number")
    elif guess > SECRET:
        print("Too low, try a higher number")
    else:
        print("Well done!  You guessed the secret number")
