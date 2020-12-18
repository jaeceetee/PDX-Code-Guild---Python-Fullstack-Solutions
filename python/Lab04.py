# Lab 04 - Magic 8-ball

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

# Give a response
print(random.choice(magic8_answers))