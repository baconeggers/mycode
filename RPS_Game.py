#!/usr/bin.env python3

"""Rock Paper Scissors Game | by TLG NDE Cohort"""

import random

def main():
    user_score = 0
    bot_score = 0
    rounds = 0
        #Main body of program
    while rounds < 3:

        choice = input("Rock, Paper, or Scissors? ").lower() #user makes choice of what to play, with input sanitization
        botchoice = random.choice(["rock", "paper", "scissors"])

        # uncomment these print functions for debug
        #print(choice)
        #print(botchoice)
        if choice not in ["rock", "paper", "scissors"]:
            print("You entered an invalid option")
            quit()

        if choice == "scissors" and botchoice == "paper":
            print("You Win!!")
            user_score += 1
            rounds +=1
            continue

        elif choice == "paper" and botchoice == "rock":
            print("You Win!!")
            user_score += 1
            rounds +=1
            continue

        elif choice == "rock" and botchoice == "scissors":
            print("You Win!!")
            user_score += 1
            rounds +=1
            continue

        else:
            print("You lost!")
            bot_score += 1
            rounds +=1
            continue
    print("Bot Score:", bot_score, "\nUser Score:" ,user_score)

main()