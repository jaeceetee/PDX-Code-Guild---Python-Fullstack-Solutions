# Lab 07 - Play Rock Paper Scissors
import random

game_choices = ['rock', 'paper', 'scissors']

# Welcome User to the game and ask for their choice
print("Lets play a game - rock, paper, or scissors")
# While loop to ask if the user wants to play again
play_again = True
while play_again == True:
    user_choice = ''
    while user_choice not in game_choices:
        user_choice = input("What's your choice?: ").lower()

    # Computer chooses randomly
    comp_choice = random.choice(game_choices)

    # See who won
    game_winner = ''
    if user_choice == comp_choice:
        game_winner = 'TIE'
    elif user_choice == 'rock':
        if comp_choice == 'scissors':
            game_winner = 'YOU'
        elif comp_choice == 'paper':
            game_winner = "COMPUTER"
    elif user_choice == 'scissors':
        if comp_choice == 'paper':
            game_winner = 'YOU'
        elif comp_choice == 'rock':
            game_winner = "COMPUTER"
    elif user_choice == 'paper':
        if comp_choice == 'rock':
            game_winner = 'YOU'
        elif comp_choice == 'scissors':
            game_winner = "COMPUTER"

    # Display the result
    result = f'Winner: {game_winner}! You had {user_choice} and computer had {comp_choice}'
    print(result)
    user_decision = input("Type Y if you want to play again: ").lower()
    if user_decision == 'y':
        play_again = True
    else:
        play_again = False
        print("Goodbye!")

    