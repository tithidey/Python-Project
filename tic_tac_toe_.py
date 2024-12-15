import random

box =  [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def printBox(box):
    line = '---+---+---'
    print(line)
    for row in box:
        print(f' {row[0]} | {row[1]} | {row[2]}')
        print(line)

printBox(box)

current_player = 'X'
computer_player = 'O'

while True:
    row = int(input('Choose between 0-2: '))
    column = int(input('Choose between 0-2: '))
    if box[row][column] == ' ':
        box[row][column] = current_player
    else:
        print('Place is already taken. Choose another spot.')
        continue

     
    print(box)



    
# userChoice = 'X'
# computerChoice = 'O'
# row, column = 3,3
# arr = [column]*row

# while True:
#     for i in range(0, column):

#         userNum = int(input("which box you want to use? row: "))
#         userNum2 = int(input("which box you want to use? column: "))
#         print(userNum, userNum2)
#         arr[userNum][userNum2] = userChoice


#     break

# for i in range(0,3):
#     print(arr)
    

    

    
