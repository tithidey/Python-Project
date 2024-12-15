import random

while True:
    n = input("Roll the dice? (y/n):")
    if n.lower() == 'y':
        print(random.sample(range(1,10),2))
    elif n.lower() == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid Choice!")