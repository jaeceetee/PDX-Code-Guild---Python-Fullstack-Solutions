# Lab 04 - Magic 8-ball - Loop until user is done

import random

# Set list to choose
magic8_answers = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
]

# Welcome user to Magic 8 Ball
print("Welcome to Magic 8 Ball!")

# Ask for their question
question = input("What is your question?: ")

# Loop
play_again = True
while play_again == True:

    # Give a response
    print(random.choice(magic8_answers))
    
    # Ask user to play again
    question = input("What is your question? or type DONE to quit: ")
    if question.lower() == "done":
        play_again = False

    