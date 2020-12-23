# Lab08 - Guess the number
import random

# Computer picks a number
comp_choice = random.randint(1,10)

# Get user guess
counter = 1
while counter < 11:
    user_choice = 0
    while user_choice not in range(1,11):
        user_choice = input("Guess the number from 1 to 10: ")
        user_choice = int(user_choice)

# Evalute 
    if user_choice == comp_choice:
        print(f"Correct! You guessed {counter} times!")
        break
    else:
        print("Try again!")
        counter += 1
else:
    print(f"You tried 10 times and did not get it! The number was {comp_choice}!")

