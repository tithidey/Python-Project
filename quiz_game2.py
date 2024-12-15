import random
# Define questions, options, correct answer
#creating list of dictionary
score = 0
quiz = [
    {
        'question': 'What is the capital of France?' ,
        'options' : ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
        'answer'  : 'C'
    },
    {
        'question' : 'Which planet is known as the red planet?',
        'options'  : ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        'answer'   : 'B'
        
    },
    {
        'question' : 'What is the largest ocean on Earth?',
        'options'  : ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
        'answer'   : 'D'
    }
]
# shuffle the questions
random.shuffle(quiz)

#loop over questions
for index, item in enumerate(quiz):
    #print question
    print(f'Question {index} : {item['question']}')
    #get user input
    for option in item['options']:
        print(option)
    answer = input('Your answer: ').upper().strip()
    #if input is correct
    if answer == item['answer']:
        print("Correct!")
        score += 1
    else:
        print(f'Wrong! The correct answer is {item['answer']}') 

print(f"Quiz over! Your final score is {score} out of {len(quiz)}")

#print correct answer
#increase score
#else
#print wrong answer
#print the final score

