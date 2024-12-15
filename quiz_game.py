answers = {
    'Question 1' : 'C',
    'Question 2' : 'B',
    'Question 3' : 'D'   
}
score = 0
while True:
    Question1 = input("Question 1: What is the capital of France?\n A. Berlin\n B. Madrid\n C. Paris\n D. Rome\n").upper()
    if Question1 == answers['Question 1']:
        print('Correct')
        score += 1
    else:
        print(f"Your answer: {Question1}")
        print(f"Wrong! The correct answer is {answers['Question 1']}")
    
    print('\n')
    
    Question2 = input("Question 2: Which planet is known as the red planet?\n A. Earth\n B. Mars\n C. Jupiter\n D. Saturn\n").upper()
    if Question2 == answers['Question 2']:
        print('Correct')
        score += 1

    else:
        print(f"Your answer: {Question2}")
        print(f"Wrong! The correct answer is {answers['Question 2']}")
    
    print('\n')

    
    Question3 = input("Question 3: What is the largest ocean on Earth?\n A. Atlantica\n B. Indian\n C. Arctic\n D. Pacific\n").upper()
    if Question3 == answers['Question 3']:
        print('Correct')
        score += 1

    else:
        print(f"Your answer: {Question3}")
        print(f"Wrong! The correct answer is {answers['Question 3']}")
    break
    
    

print(f"Quiz over! Your score is {score} over 3. 🫶🏻")                                                                                                                                                                                                                                      