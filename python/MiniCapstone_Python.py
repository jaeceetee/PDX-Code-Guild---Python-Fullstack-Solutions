# Mini capstone - Trivia game
# This will be an app that the moderator can use to get trivia questions, keep teams and scores

import requests
import json
import random
import os

#from requests.api import get

class TriviaTeams:
    def __init__(self, name = 'No Name'):
        self.name = name
        self.points = 0
    def __str__(self):
        return f"{self.name} with {self.points} points."

def reset_setting():
    setting = {
        'menu': ['1', '2'], # 1 = New Game, 2 = Exit
        'menu_select': '',
        'players': [str(i) for i in range(1,11)],
        'players_select': 0,
        'categories': [],    
        'category_select': {},
        'category_name': '',
        'questions': []
        }
    players = []
    return setting

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def get_data(url, data):
    response = requests.get(url)
    response.encoding = 'utf-8'    
    json_data = json.loads(response.text)
    return [items for items in json_data[data]]

setting = reset_setting()

# Welcome Text
print("Welcome to Trivia!")

# Set up menu
while setting['menu_select'] != '2':
    setting = reset_setting()
    players = []

    # Top level menu
    while setting['menu_select'] not in setting['menu']:
        setting['menu_select'] = input("""Please type from following options
        1 .New Game
        2. Exit
""").upper()
        if setting['menu_select'] not in setting['menu']:
            print("Invalid Entry")
        elif setting['menu_select'] == '2':
            print("Goodbye~!")

    # New Game menu
    if setting['menu_select'] == '1':
        while setting['players_select'] not in setting['players']:
            setting['players_select'] = input('How many teams? (1-10): ')
            if setting['players_select'] in setting['players']:
                setting['players_select'] = int(setting['players_select'])
                break
            else:
                print("Invalid choice")
            
        # Build Teams
        while len(players) < setting['players_select']:
            name = input(f"Enter team {len(players) + 1}: ")
            players.append(TriviaTeams(name))
        
        # Display Team Names
        for idx in range(len(players)):
            print(f"Team {idx + 1}: {players[idx].name}")
        input("Enter to continue...")
        screen_clear()
        

        # Get Questions
        url = 'https://opentdb.com/api_category.php'
        setting['categories'] = get_data(url, 'trivia_categories')

        # Pick a Category
        for idx in range(len(setting['categories'])):
            print(f"{idx + 1}. {setting['categories'][idx]['name']}")
        
        while setting['category_select'] not in setting['categories']:
            current_category = input(f"Enter the number for the category you would like to play [1 - {len(setting['categories'])}]: ")
            if current_category.isdigit() == True:
                for cat in setting['categories']:
                    if int(current_category) + 8 == int(cat['id']):
                        setting['category_select'] = cat
                        break
                else:
                    print("Invalid input")
            else:
                print("Invalid input")

        # Get Questions
        url = 'https://opentdb.com/api.php?amount=10&category=' + str(setting['category_select']['id'])
        setting['questions'] = get_data(url, 'results')

        # PLAY GAME
        for question in setting['questions']:
            screen_clear()
            if question['type'] == 'boolean':
                print("True or False")
                print(question['question'])
                input("Press Enter for answer...")
                print(question['correct_answer'] + "\n\n")
            else:
                print("Multiple Choice")
                print(question['question'])
                choices = question['incorrect_answers']
                choices.append(question['correct_answer'])
                random.shuffle(choices)
                for idx in range(len(choices)):
                    print(f"{idx + 1}. {choices[idx]}")
                input("Press Enter for answer...")
                for idx in range(len(choices)):
                    if choices[idx] == question['correct_answer']:
                        print(f"{idx + 1}. {choices[idx]}\n\n")
            if len(players) == 1:
                answer = input(f"Point for Team {players[0].name}? (Y for point): ").upper()
                if answer == 'Y':
                    players[0].points += 1
            else:
                for idx in range(len(players)):
                    print(f"Team {idx + 1}: {players[idx].name}")
                teams_with_points = []
                confirmed = False
                while confirmed == False:
                    points = input("Winning teams: Enter tean NUMBERS separated by a SPACE: ")
                    if len(points) < 1:
                        pass
                    elif points.find(' ') != -1:
                        teams_with_points = points.split(' ')
                    elif points.isdigit() == True:
                        teams_with_points.append(points)
                    else:
                        print('invalid entry')
                        continue

                    if len(teams_with_points) < 1:
                        reply = input("No teams get points? (Y = confirm, other keys go back.): ").upper()
                        if reply == 'Y':
                            confirmed = True
                    else:
                        print("Following teams will get points:")
                        for idx in range(len(players)):
                            if str(idx + 1) in teams_with_points:
                                print(f"Team {idx + 1}: {players[idx].name}")
                        reply = input("Is this correct? (Y = confirm, other keys go back.): ").upper()
                        if reply == 'Y' and len(teams_with_points) >= 1:
                            for team in teams_with_points:
                                players[int(team) - 1].points +=1
                            confirmed = True
                        else:
                            teams_with_points = []

        # Rank teams
        screen_clear()
        if len(players) == 1:
            print(f"You got {players[0].points} out of 10 correct!")
        else:
            print("The team scores are:")
            players = sorted(players, key=lambda x: x.points, reverse=True)
            for player in players:
                print(player) 
    
    # Clear settings for a new game
