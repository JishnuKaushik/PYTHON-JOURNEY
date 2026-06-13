# Python quiz game :

questions = ("How many elements are in the periodic table ?: ", 
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas is Earth's atmosphere?: ",
             "How many bones are there in human body?: ",
             "Which part in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)
        
    guess = input("What do you think is crct ans to this question : ").upper()# we added .upper so that upper case and lower case dont cause any trouble.
    guesses.append(guess) 
    if guess == answers[question_num]:
        score += 1
        print("correct")

    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct ans")    
    question_num += 1    
        
print("--------------------------------------------------------------------")        
print("-------------------------------RESULT-------------------------------")
print("--------------------------------------------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}")