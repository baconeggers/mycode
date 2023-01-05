#!/usr/bin/env

"""Small videogame trivia quiz made as a side project | Charles M Eggers II"""

import question_bank        # importing the questions and answers from another module
import time                 # importing the time module to add a second of sleep between questions

q_list=list(question_bank.all_questions)                # places all questions into a list
a_list=list(question_bank.all_questions.values())       # places the answer options [A,B,C,D] into a list
rounds = 0                  # preset value for total number of rounds
score = 0                   # preset value for total score

def quiz():                 # intro/outro for the quiz
    print("Welcome to the Videogame Trivia Quiz")
    print("Type A, B, C, or D to answer a question.\nOr type 'Q' to quit")
    time.sleep(1)           # quick computer nap to give space to read
    for questions in q_list:
        question()
    print("Thank you for playing! Your final score is:", score)

def question():             # the meat and potatoes of the quiz program
    global a_list
    global q_list           # pulling the previously set global variables for use in the function
    global rounds
    global score
    while rounds < 10:          # while loop to keep the game going after a question
        try:
            print(q_list[0])        # prints the question at q_list position [0]
            print(a_list[0])        # prints the multiple choice answers at a_list position [0]
            user_answer = input("Answer: ").upper()         # user input for their guess
            if user_answer in ["QUIT", "Q"]:                # can be called at any time to quit
                print("Thanks for playing!")
                quit()
            elif user_answer not in ["A","B","C","D"]:        # input validation
                print("You have entered an invalid option")
                continue
            elif user_answer == question_bank.answers[0]:   # checks user's guess against the answers listed in the imported question bank
                print("Correct!")
                a_list.pop(0)                               # pops the multiple choice answers from a_list, moving the queue forward
                question_bank.answers.pop(0)                # same, but for the actual correct answer
                q_list.pop(0)                               # same, but this time for the questions
                rounds += 1                                 # moves the round counter up
                score += 1                                  # adds to the user score
            else:
                print("Sorry, the correct answer was", question_bank.answers[0])        # if the user's guess is wrong, the quiz lets them know
                a_list.pop(0)                               # still gotta move those queues forward
                question_bank.answers.pop(0)
                q_list.pop(0)
                rounds +=1                                  # add a round, but no score
            time.sleep(1)                                   # adds a small pause between questions, makes it feel better, ya know?
        except Exception as err:
            print("Dang, you found a hole in my validation", err)
if __name__ == "__main__":
    quiz()                      # if i ever decide to steal a variable or function from here, this will help prevent the import running the entire thing