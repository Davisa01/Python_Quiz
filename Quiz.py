questions = ("How many bones is in the human body?",
             "Which animal lays the largest egss? ",
             "What is the most abundant gas in Earth's atmosphere? ",
             "How many element is in the periodic table ")
options = (("A. 116", "B. 118", "C. 206", "D. 208"),
           ("A. Whale", "B. Crocodile", "C. Ostrich", "D. Elephant"),
           ("A. Nitrogen", "B. Oxygen", "C. Cardon-Dioxide", "D. Hydrogen"),
           ("A. 118", "B. 109", "C. 110", "D. 115"))


answers = ("C", "C", "A", "A")

guesses = []
score = 0
question_num = 0

# print(--------------------------------------)
for question in questions:
    print('--------------------------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter the answer(A, B, C, D) ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
        



print()
print('-------------------------------------')
print("              RESULT                 ")
print('-------------------------------------')
print()


print(f"You score {int(score)}/{question_num}")
print(f"The answers are {answers}")
print(f"You choose {guesses}")


