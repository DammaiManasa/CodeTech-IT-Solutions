#Quiz_application
intro="""
Welcome to the Quiz Application!You will be asked multiple-choice questions from various categories.
Please select the correct option (A/B/C/D) for each question.Let's begin!\n
            """
print(intro)
questions = {
    "How many days does it take for the Earth to orbit the Sun ?": ["A.366", "B. 365", "C. 367", "D. 364"],
    "Which keyword is used for function in python language ?": ["A.function", "B.def", "C.Fun", "D.Define"],
    "What is the chemical symbol for water?": ["A. Ho2", "B. H2o", "C. O2", "D. Wt"],
    "Who is the father of AC voltage?": ["A. Thomas Alva Edison", "B. Nichola Tesla", "C. Michael Faraday", "D. Friedrich Lenz"],
    "How lond does it take to sing national anthem?": ["A. 54sec ", "B.52sec", "C. 55sec", "D. 58 sec"] } #quiz questions taken in dict

# defining a Function to ask questions and to trace score
def quiz_application():
    score = 0
    total_questions = len(questions)
    for question in questions.keys(): #iterating to display questions on the console
        print(question)
        for choice in questions[question]: #iterating to display choices on the console
            print(choice)
        user_answer = input("Your answer (A/B/C/D): ").upper() #taking user input

        # Checking if answer is correct and then updating the score
        if user_answer == "A" or user_answer == "B" or user_answer == "C" or user_answer == "D":
            if questions[question][ord(user_answer) - 65].startswith('B'):
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        else:
            print("Invalid choice. Skipping question...")

    #providing feedback based on the total score secured
    if score==0:
     print("OOPS! You lose")
     print("Your score is:", score, "out of", total_questions)
     print("Better Luck for next time")
    if score>0 or score<5:
     print("GOOD JOB!")
     print("Your score is:", score, "out of", total_questions)
     print("Better Luck for next time")
    if score==5:
     print("CONGRATULATIONS! You WON")
     print("Your score is:", score, "out of", total_questions)
     
    print("Quiz completed!")


quiz_application()#calling quiz_application 

