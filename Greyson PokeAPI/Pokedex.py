import requests
import json
from sys import exit
#function library

#gets the type(s) of the pokemon
def pokeType():
    print(f"{coolPokemon.title()} is a", end = " ")
    for i in pokeInfo['types']:
        if i['slot'] == 1:
            print(i['type']['name'].title(), end = " ")
        if i['slot'] == 2:
            print('and', i['type']['name'].title(), end = " ")
    print('type')
    print('')

#gets what evolves into the pokemon (if any) what the pokemon evolves to (if any) and what the methods are (if any)
def pokeEvolve():
    pokeSpecies = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{coolPokemon}").json()['evolution_chain']['url']
    pokeEvo = requests.get(pokeSpecies).json()
    if len(pokeEvo['chain']['evolves_to']) == 0:
        print("The only pokemon in the species is ", end = "")
    else:
        print("The first pokemon in the species is ", end = "")
    print(pokeEvo['chain']['species']['name'].title(), end = "")
    #gets all the evolution details
    if pokeEvo['chain']['evolves_to'] != []:
        print(", which evolves into")
    for i in pokeEvo['chain']['evolves_to']:
        extras = ""
        min_level = ""
        item = ""
        print(i['species']['name'].title(), end = f" by ")
        try:
            for e in i['evolution_details'][0]:
                evoDetails = i['evolution_details'][0][e]
                if evoDetails != None and evoDetails != False and evoDetails != '':
                    #print(e, evoDetails['name'], end = " ")
                    if e == "trigger":
                        if evoDetails['name'] == 'level-up':
                            if min_level != '':
                                trigger = f"getting to level {min_level}"
                            else:
                                trigger = f"levelling up"
                                if True:
                                    pass
                        elif evoDetails['name'] == 'use-item':
                            trigger = f"using a {item}"
                        elif evoDetails['name'] == "take-damage":
                            trigger = "running under the stone arch in the Dusty Bowl zone of the wild area, while missing at least 49 hp"
                        elif evoDetails['name'] == "shed":
                            trigger = f"having an empty slot and an extra pokeball when {coolPokemon.title()} evolves"
                        elif evoDetails['name'] == "trade":
                            trigger = "being traded"
                        elif evoDetails['name'] == "three-critical-hits":
                            trigger = "hitting three critical hits in one battle"
                        elif evoDetails['name'] == "spin":
                            trigger = "spinning"
                        else:
                            trigger = (e, evoDetails)
                    elif e == "min_level":
                        min_level = evoDetails
                    elif e == "item":
                        item = evoDetails['name'].replace('-', ' ').title()
                    elif e == 'min_happiness':
                        extras += f"with a happiness of {evoDetails} "
                    elif e == 'time_of_day':
                        extras += f"at {evoDetails}time "
                    elif e == "location":
                        extras += f"at {evoDetails['name'].replace('-', ' ').title()} "
                    elif e == "known_move_type":
                        extras += f"knowing a {evoDetails['name']} type move "
                    elif e == "min_affection":
                        extras += f"with a minimum affection of {evoDetails} "
                    elif e == "turn_upside_down":
                        if evoDetails == True:
                            extras += "while the console is upside down"
                    elif e == 'party_type':
                        extras += f"with a {evoDetails['name']} type in the party"
                    elif e == 'min_beauty':
                        extras += f"with a minimum beauty of {evoDetails}"
                    elif e == "relative_physical_stats":
                        if evoDetails == -1:
                            extras += "while having a higher defense than attack"
                        else:
                            extras += "while having a higher attack than defense"
                    elif e == "party_species":
                        extras += f"while having a {evoDetails['name'].title()} in the party"
                    elif e == "held_item":
                        extras += f"while holding a {evoDetails['name'].replace('-', ' ').title()} "
                    elif e == "known_move":
                        extras += f"while knowing the move \"{evoDetails['name']}\""
                    elif e == "gender":
                        if evoDetails == 1:
                            extras += "if it's a female"
                        else:
                            extras += "if it's a male"
                    elif e == "needs_overworld_rain":
                        if evoDetails:
                            extras += "while it is raining"
                    else:
                        print(e, evoDetails, end = " ")
        except:
            print("This pokemon has no evolution data available")
        if i['species']['name'] == "hitmontop":
            extras += "while having an equal defense and attack"
        response = f"{trigger} {extras}"
        print(response)     
        try:
            for j in i['evolves_to']:
                trigger = ""
                extras = ""
                min_level = ""
                for e in j['evolution_details'][0]:
                    evoDetails = j['evolution_details'][0][e]
                    if evoDetails != None and evoDetails != False and evoDetails != '':
                        if e == "trigger":
                            if evoDetails['name'] == 'level-up':
                                if min_level != '':
                                    trigger = f"getting to level {min_level}"
                                else:
                                    trigger = f"levelling up"
                                    if True:
                                        pass
                            elif evoDetails['name'] == 'use-item':
                                trigger = f"using a {item}"
                            elif evoDetails['name'] == "take-damage":
                                trigger = "running under the stone arch in the Dusty Bowl zone of the wild area, while missing at least 49 hp"
                            elif evoDetails['name'] == "shed":
                                trigger = f"having an empty slot and an extra pokeball when {coolPokemon.title()} evolves"
                            elif evoDetails['name'] == "trade":
                                trigger = "being traded"
                            elif evoDetails['name'] == "three-critical-hits":
                                trigger = "hitting three critical hits in one battle"
                            elif evoDetails['name'] == "spin":
                                trigger = "spinning"
                            else:
                                trigger = (e, evoDetails)
                        elif e == "min_level":
                            min_level = evoDetails
                        elif e == "item":
                            item = evoDetails['name'].replace('-', ' ').title()
                        elif e == 'min_happiness':
                            extras += f"with a happiness of {evoDetails} "
                        elif e == 'time_of_day':
                            extras += f"at {evoDetails}time "
                        elif e == "location":
                            extras += f"at {evoDetails['name'].replace('-', ' ').title()} "
                        elif e == "known_move_type":
                            extras += f"knowing a {evoDetails['name']} type move "
                        elif e == "min_affection":
                            extras += f"with a minimum affection of {evoDetails} "
                        elif e == "turn_upside_down":
                            if evoDetails == True:
                                extras += "while the console is upside down"
                        elif e == 'party_type':
                            extras += f"with a {evoDetails['name']} type in the party"
                        elif e == 'min_beauty':
                            extras += f"with a minimum beauty of {evoDetails}"
                        elif e == "relative_physical_stats":
                            if evoDetails == -1:
                                extras += "while having a higher defense than attack"
                            else:
                                extras += "while having a higher attack than defense"
                        elif e == "party_species":
                            extras += f"while having a {evoDetails['name'].title()} in the party"
                        elif e == "held_item":
                            extras += f"while holding a {evoDetails['name'].replace('-', ' ').title()} "
                        elif e == "known_move":
                            extras += f"while knowing the move \"{evoDetails['name']}\""
                        elif e == "gender":
                            if evoDetails == 1:
                                extras += "if it's a female"
                            else:
                                extras += "if it's a male"
                        elif e == "needs_overworld_rain":
                            if evoDetails:
                                extras += "while it is raining"
                        else:
                            print(e, evoDetails, end = " ")
                response = f"{trigger} {extras}"
                if j == i['evolves_to'][0]:
                    print(f"which evolves into {j['species']['name'].title()} by" , end = " ")
                else:
                    print(f"or evolves into {j['species']['name'].title()} by", end = " ")
                print(response)
        except:
            pass
    print('')

#gets the egg group the pokemon is in
def pokeEggGroup():
    print(f"{coolPokemon.title()}'s egg group is", end = " ")
    eggGroup = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{coolPokemon}/").json()["egg_groups"][0]["name"]
    try:
        int(eggGroup[-1])
        eggList = list(eggGroup)
        eggList.insert(-1, " ")
        eggGroup = "".join(eggList)
    except:
        pass
    print(eggGroup.title())
    print('')
#gets the height and weight of the pokemon
def pokeHeightWeight():
    height = str(requests.get(f"https://pokeapi.co/api/v2/pokemon/{coolPokemon}/").json()['height'] / 3.048)
    weight = str(requests.get(f"https://pokeapi.co/api/v2/pokemon/{coolPokemon}/").json()['weight'] / 4.5359237)
    print(f"{coolPokemon.title()} is {height[:4]} feet tall")
    print('')
    print(f"{coolPokemon.title()} weighs {weight[:6]} pounds")
    print('')
#end of the function library

#gets the pokemon the user wants information on
coolPokemon = input("Please input a pokemon: ").lower()
#reads a file i have to get a big list of all the pokemons names and there corresponding url to access the information, e.g.: {'name': 'garchomp', 'url': 'https://pokeapi.co/api/v2/pokemon/445/'}
with open('D:\Code Stuff\Python Project\File Storage\Pokemon Names.txt') as pokeNameStorage:
    pokeList = json.loads(pokeNameStorage.read())
for i in pokeList:
    if i['name'] == coolPokemon:
        pokeDict = i
        break
try:
    pokeInfo = requests.get(pokeDict['url']).json()
except:
    print("No data is available on this pokemon, or this is a typo")
    exit()

print('')

pokeEvolve()
pokeType()
pokeEggGroup()
pokeHeightWeight()
