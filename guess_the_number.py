import random

guess = random.randint(1,100)

while True:
    n = int(input("Guess the number between 1 and 100: "))
    if n > guess:
        print("Too High!")
    elif n < guess:
        print("Too Low!")
    else:
        print("Congratulations! You guessed the number.")
        break