import requests

import random

# Base url to store url
base_url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?'

# List of the types we're getting
type_list = ['Spellcaster', 'Dragon', 'Warrior', 'Cyberse', 'DIVINE-BEAST']

# dict where everything will go
mon_dict = {}

# For loop goes through each monster type and adds them to seperate dicts in mon_dict
for i in type_list:
    mon_dict[i] = {}
    complete_url = base_url + "race=" + i
    response = requests.get(complete_url).json()
    for j in range(len(response['data'])):
        mon_dict[i][response['data'][j]['name']] = response['data'][j]['atk']


def game_on():
    player_one_lp = 4000
    player_two_lp = 4000

    while True:
        print("Monster Types to choose from:")
        print(*mon_dict, sep=', ')
        player1_choice = input('Player 1\'s Monster Type: ')
        player2_choice = input('Player 2\'s Monster Type: ')

        # Player 1's random monster and it's atk
        rand_play1 = random.randint(0, len(mon_dict[player1_choice].keys()) - 1)
        keys = list(mon_dict[player1_choice].keys())
        name1 = keys[rand_play1]
        atk1 = mon_dict[player1_choice][name1]

        # Player 2's random monster and it's atk
        rand_play2 = random.randint(0, len(mon_dict[player2_choice].keys()) - 1)
        keys = list(mon_dict[player2_choice].keys())
        name2 = keys[rand_play2]
        atk2 = mon_dict[player2_choice][name2]

        # Prints their monsters and atk to the screen
        print("Player 1's monster:", name1, "ATK:", atk1, "\n" + "Player 2's monster:", name2, "ATK:", atk2)

        # Check who won and change LP
        if int(atk1) > int(atk2):
            player_two_lp = player_two_lp - (int(atk1) - int(atk2))
            print("Player 1 wins the round. \nPlayer 1's LP:", player_one_lp, "\nPlayer 2's LP:", player_two_lp)
        elif int(atk2) > int(atk1):
            player_one_lp = player_one_lp - (int(atk2) - int(atk1))
            print("Player 2 wins the round. \nPlayer 1's LP:", player_one_lp, "\nPlayer 2's LP:", player_two_lp)
        elif int(atk1) == int(atk2):
            print("Its a draw. \nPlayer 1's LP:", player_one_lp, "\nPlayer 2's LP:", player_two_lp)

        # Make it look nice
        print()

        # Check if game is over
        if player_one_lp <= 0:
            break
        elif player_two_lp <= 0:
            break

    if player_one_lp <= 0:
        return "Player Two Wins!"
    elif player_two_lp <= 0:
        return "Player One Wins!"


# Function for creating a file
def make_file(txt, name='monsters.txt'):
    with open(name, 'w') as file:
        file.write(txt)


# Function for reading from file
def open_file(name='monsters.txt'):
    with open(name, 'r') as file:
        line = file.readline()
        return line


# Puts the stuff from the dictionary to the file
def use_file():
    card_name = input("Enter a card name: ")
    complete = base_url + "name=" + card_name
    resp = requests.get(complete).json()
    card_text = resp['data'][0]['name'] + ": " + resp['data'][0]['desc']
    make_file(card_text)
    print(open_file())


print(game_on())
print()
use_file()
