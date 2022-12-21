#!/usr/bin/env python3

import html

def main():

    trivia = {
             "category": "Entertainment: Film",
             "type": "multiple",
            "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
            "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
            "incorrect_answers": [
                "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
                "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
                "&quot;Round up the usual suspects.&quot;"
                ]
            }   


    print("Movie Trivia!")
    print("Question 1:")
    print(trivia["question"]) 
    print("A.", html.unescape(trivia["correct_answer"]))
    print("B.", html.unescape(trivia["incorrect_answers"][0]))
    print("C.", html.unescape(trivia["incorrect_answers"][1]))
    print("D.", html.unescape(trivia["incorrect_answers"][2]))

    user_answer = input("Answer: ")

    if user_answer == "A":
        print("That is correct!")
    else:
        print("Sorry, that is incorrect.")
        retry = input("Try again? ").lower()
        if retry == "yes":
                main()      
        else:
            quit()

if __name__ == "__main__":
    main()