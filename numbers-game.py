#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

def main():
    num = random.randint(1,100)

    rounds = 0

    guess = " "

    while rounds < 5 and guess != num:
        rounds += 1
        guess = int(input("Guess a number between 1 and 100\n"))

        if guess == num:
            print("Correct!")

        elif rounds == 5:
            print("Sorry, the correct answer was ", num)

        elif guess < num:
            print("Too low!")

        elif guess > num:
            print("Too high!")

if __name__ == "__main__":
    main()