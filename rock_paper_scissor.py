import random

emojis = {'r':'🪨', 'p': '📃', 's':'✂️'}
choices = ['r','p','s']
computer_choice = ''
while True:


    users = input("Rock/Paper/Scissor ? r/p/s: ").lower()

    if users not in choices:
        print("Invalid choice!")
    else:

        computer_choice = random.choice(choices)
        print(f"You choose: {emojis[users]}")
        print(f"Computer choose: {emojis[computer_choice]}")
       
        if users == 'r' and computer_choice == 'p' or users == 'p' and computer_choice == 's' or users == 's' and computer_choice == 'r':
            print("You lose!")
        elif users == computer_choice:
            print('Tie')
        else:
            print("You win!")

    ask_to_continue = input("Do you want to play again? y/n: ")
    if ask_to_continue == 'n':
        break
    elif ask_to_continue != 'n' or ask_to_continue != 'y':
        print("Invalid input!")
    else:
        continue
    