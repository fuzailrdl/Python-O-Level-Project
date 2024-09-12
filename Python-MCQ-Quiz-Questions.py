# O Level M3 R5.1 Project with Python in MCQ Quiz Game.

questions = ("1. Which one of the following is not a keyword in Python language?: ",
            "2. Which of the following statements is used to create an empty set in Python?: ",
            "3. To add a new element to a list we use which Python command?: ",
            "4. What is the maximum possible length of an identifier in Python?: ",
            "5. Which of the following is a Python tuple?: ",
            "6. Who developed Python Programming Language?: ",
            "7. Which type of Programming does Python support?: ",
            "8. Is Python case sensitive when dealing with identifiers?: ",
            "9. Which of the following is the correct extension of the Python file?: ",
            "10. Is Python code compiled or interpreted?: ")


options = (("A. pass",
             "B. eval",
             "C. assert",
             "D. nonlocal"),


            ("A. ()",            
             "B. []",
             "C. { }",
             "D. set()"),


            ("A. list1.addEnd(5)",
             "B. list1.addLast(5)",
             "C. list1.append(5)",
             "D. list1.add(5)"),


            ("A. 79 characters",
             "B. 59 characters",
             "C. 67 characters",
             "D. none of the mentioned"),


            ("A. {1, 2, 3}",
             "B. { }",
             "C. [1, 2, 3]",
             "D. (1, 2, 3)"),
             
             
            ("A. Wick van Rossum",
             "B. Rasmus Lerdorf",
             "C. Guido van Rossum",
             "D. Niene Stom"),


            ("A. object-oriented programming",
             "B. structured programming",
             "C. functional programming",
             "D. all of the mentioned"),
             
             ("A. no",
              "B. yes",
              "C. Machine Dependent",
              "D. none of the mentioned"),
             
             ("A. .python",
              "B. .pl",
              "C. .py",
              "D. .p"),
             
             ("A. Python code is both compiled and interpreted",
              "B. Python code is neither compiled nor interpreted",
              "C. Python code is only compiled",
              "D. Python code is only interpreted"))

answers = ("B", "D", "C", "D", "D", "C", "D", "B", "C", "A")

explanations = ("Explanation: eval can be used as a variable.",
                

                "Explanation: { } creates a dictionary not a set. Only set() creates an empty set.",


                "Explanation: We use the function append to add an element to the list.",


                "Explanation: Identifiers can be of any length.",


                "Explanation: Tuples are represented with round brackets.",


                "Explanation: Python language is designed by a Dutch programmer Guido van Rossum in the Netherlands.",


                """Explanation: Python is an interpreted programming language, which supports object-oriented,
structured, and functional programming.""",


                "Explanation: Case is always significant while dealing with identifiers in python.",


                """Explanation: ‘.py’ is the correct extension of the Python file.Python programs can be written in any text editor.
To save these programs we need to save in files with file extension ‘.py’.""",


                "Explanation: Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python.")

guesses = []

score = 0

questionNum = 0

for question in questions:
    print("--------------------------------------------------------------------------------------")
    print(question)
    print("--------------------------------------------------------------------------------------")
    for option in options[questionNum]:
        print(option)
    print("____________________________")
    guess = input("Enter Option 'A','B','C','D': ").upper()
    guesses.append(guess)
    if guess == answers[questionNum]:
        print("✅ CORRECT...")
        print("____________________________")
        score += 1
    else:
        print("❌ WRONG")
        print(f"'{answers[questionNum]}' is a right answer")
        # print("--------------------------------------------------------------------------------------")
        print(f"➡ {explanations[questionNum]}")
        print()
    questionNum += 1

print()
print("-----------------------------------------")
print("RESULTS".center(41))
print("-----------------------------------------")
print()

print("Answer Key: ",end=" ")

for answer in answers:
    print(answer,end=" ")

print()

print("You Guessed: ",end=" ")

for guess in guesses:
    print(guess,end=" ")
print()

print(f"Your total correct answer is: {score} out of 10")
score = score / len(questions) * 100
print(f"Your Score is: {int(score)}%")