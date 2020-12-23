# Lab08_v5 - Guess the number - Computer guesses what human inputs

import random
valid_options = []
# Number Set
n = 10
for i in range(n):
    valid_options.append(str(i + 1))

print(valid_options)


# Get user number
user_input = 0
while user_input not in valid_options:
    user_input = input("Pick a number from 1 to 10: ")

user_input = int(user_input)

# Conputer guesses
comp_guess = random.randint(1,10)
counter = 1
while user_input != comp_guess:
    if user_input < comp_guess:
        result = f"Computer guessed {comp_guess}. Too high, trying again!"
    else:
        result = f"Computer guessed {comp_guess}. Too low, trying again!"
    counter +=1
    print(result)
    comp_guess = random.randint(1,10)
else:
    print(f"{comp_guess} is correct! It guessed {counter} times!")