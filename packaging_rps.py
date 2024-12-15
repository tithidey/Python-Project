import random
class Game:
    emojis = {'r':'🪨', 'p': '📃', 's':'✂️'}
    choices = ['r','p','s']
    computer = random.choice(choices)
    def __init__(self, userChoice):
        self.userChoice = userChoice.lower()

        

    def printChoice(self):
        if self.userChoice not in self.choices:
            print("Invalid choice!")
        else:
            print(f"You choose: {self.emojis[self.userChoice]}")
            print(f"Computer choose: {self.emojis[self.computer]}")

    def askPermission():
        ask = input("Do you want to resume?")


    def rock_paper_scissor(self):  
        if self.userChoice == 'r' and self.computer == 'p' or self.userChoice== 'p' and self.computer == 's' or self.userChoice == 's' and self.computer == 'r':
            print("You lose!")
        elif self.userChoice == self.computer:
            print('Tie')
        else:
            print("You win!")

game = Game('r')
game.printChoice()
game.rock_paper_scissor()
