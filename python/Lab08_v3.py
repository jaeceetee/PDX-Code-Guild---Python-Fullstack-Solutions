# Lab08_v3 - Guess the number
import random

# Computer picks a number
comp_choice = random.randint(1,10)

# Get user guess
counter = 0
user_choice = 0

# Evaluate
while user_choice != comp_choice:
    if counter != 0:
        if user_choice > comp_choice:
            print("Too high! Try again!")
        else:
            print("Too low! Try again!")
    counter += 1
    user_choice = 0
    while user_choice not in range(1,11):
        user_choice = input("Guess the number from 1 to 10: ")
        user_choice = int(user_choice)
else:
    print(f"Correct! You guessed {counter} times!")
