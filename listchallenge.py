#!/usr/bin/env python3

heroes = ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite Character is Black Panther!

print("My favorite character is", heroes[0])


# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.

choice = int(input("Pick a number between 1 and 100: "))
print(choice)


nums = [1, -5, 56, 987, 0]

# PART 3
# check out https://docs.python.org/3/library/function.html or go to Google
# use a built-in function to find out which integer in nums is the biggest.
# then, print out that number!

print(max(nums))
