# Lab08_v4 - Guess the number
import random

# Computer picks a number
comp_choice = random.randint(1,10)

counter = 0
user_choice = 0
last_guess_target = 11
current_guess_target = 0
result =''

# Get user input/Evaluate
while user_choice != comp_choice:

    counter += 1
    user_choice = 0
    while user_choice not in range(1,11):
        user_choice = input("Guess the number from 1 to 10: ")
        user_choice = int(user_choice)
    current_guess_target = abs(comp_choice - user_choice)

    if user_choice != comp_choice:
        if counter != 1:
            if current_guess_target < last_guess_target:
                result = "Closer but still "
            elif current_guess_target > last_guess_target:
                result = "Further and "
            else:
                result = "You typed same number! It is "
            if user_choice > comp_choice:
                result += "too high! Try again!"
            elif user_choice < comp_choice:
                result += "too low! Try again!"
            print(result)
           
        else:
            if user_choice > comp_choice:
                print("Too high! Try again!")
            else:
                print("Too low! Try again!")
    last_guess_target = current_guess_target
else:
    print(f"Correct! You guessed {counter} times!")
