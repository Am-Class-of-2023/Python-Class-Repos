#import requests
import json

base_url = 'https://mhw-db.com/'
type = input('Enter the desired data type (weapons, monsters, armor): ').lower()
url = base_url + type

#database = requests.get(url).json()
#print(database)

#with open('D:\MHWArmor.txt', 'w') as databaseStorage:
    #databaseStorage.write(requests.get(url).json())


def findMonster():
    monster = input('Enter the monster you would like to find: ').title()
    for i in range(len(database)):
        if database[i]['name'] == monster:
            monsterInfo = database[i]
            #print(monsterInfo)

    locations = [monsterInfo['locations'][i]['name'] for i in range(len(monsterInfo['locations']))]
    weaknesses = [monsterInfo['weaknesses'][i]['element'] for i in range(len(monsterInfo['weaknesses'])) if monsterInfo['weaknesses'][i]['stars'] == 3]
    if weaknesses == []:
        weaknesses = ['None']
    resistances = [monsterInfo['resistances'][i]['element'] for i in range(len(monsterInfo['resistances']))]
    if resistances == []:
        resistances = ['None']

    print('\n')
    print('Monster name: ' + monsterInfo['name'])
    print('Type: ' + monsterInfo['species'].title())
    print('Description: ' + monsterInfo['description'])
    print('Found in: ', end='')
    print(*locations, sep=', ')
    print('Weaknesses: ', end='')
    print(*weaknesses, sep=', ')
    print('Resistances: ', end='')
    print(*resistances, sep=', ')
    print('\n')


def findWeapon():
    weaponsList = []
    weaponType = input('Enter the type of weapon you want: ').lower().replace(' ', '-')
    for i in range(len(database)):
        if database[i]['type'] == weaponType:
            weaponsList.append(database[i])
    #print(weaponsList)
    weapon = input('Enter the specific weapon you want: ').title()
    for i in range(len(weaponsList)):
        if weaponsList[i]['name'] == weapon:
            weaponInfo = weaponsList[i]
            #print(weaponInfo)
    
    if weaponInfo['elements'] == []:
        elements = 'None'
    else:
        elements = weaponInfo['elements'][0]['type'].title()
    
    for key, value in weaponInfo['durability'][0].items():
        if value == 0:
            break
        else:
            sharpness = key

    if weaponInfo['attributes'] == {}:
        affinity = 0
    else:
        affinity = weaponInfo['attributes']['affinity']
    
    materials = {}
    if weaponInfo['crafting']['craftable'] == True:
        for i in range(len(weaponInfo['crafting']['craftingMaterials'])):
            materials[weaponInfo['crafting']['craftingMaterials'][i]['item']['name']] = weaponInfo['crafting']['craftingMaterials'][i]['quantity']
    else:
        for i in range(len(weaponInfo['crafting']['upgradeMaterials'])):
            materials[weaponInfo['crafting']['upgradeMaterials'][i]['item']['name']] = weaponInfo['crafting']['upgradeMaterials'][i]['quantity']

    print('\n')
    print('Weapon: ' + weaponInfo['name'])
    print('Damage: ' + str(weaponInfo['attack']['display']))
    print('Affinity: ' + str(affinity))
    print('Highest sharpness: ' + sharpness.title())
    if weaponType == 'charge-blade':
        print('Phial type: ' + weaponInfo['phial']['type'])
    print('Element: ' + str(elements))
    print('Elderseal: ' + str(weaponInfo['elderseal']).title())
    print('Crafting materials: ', end='')
    craftingMaterials = ''
    print('Crafting materials: ', end='')
    for item, quantity in materials.items():
        craftingMaterials += str(item) + " " + str(quantity) + "x, "
    print(craftingMaterials[:-2])
    print('\n')


def findArmor():
    armorList = []
    armorType = input('Enter the type of armor you want(ex: head): ')
    for i in range(len(database)):
        if database[i]['type'] == armorType:
            armorList.append(database[i])
    #print(armorList)
    armor = input('Enter the specific piece of armor you want: ').title()
    for i in range(len(armorList)):
        if armorList[i]['name'] == armor:
            armorInfo = armorList[i]
    #print(armorInfo)

    skills = [armorInfo['skills'][i]['skillName'] for i in range(len(armorInfo['skills']))]
    resistances = armorInfo['resistances']

    print('\n')
    print('Piece name: ' + armorInfo['name'])
    print('Defense: ' + str(armorInfo['defense']['base']))
    resistancesStr = ''
    print('Resistances: ', end='')
    for element, resistance in resistances.items():
        resistancesStr += str(element) + ": " + str(resistance) + ", "
    print(resistancesStr[:-2])
    print('Skills: ', end='')
    print(*skills, sep=', ')
    materials = {}
    for i in range(len(armorInfo['crafting']['materials'])):
        materials[armorInfo['crafting']['materials'][i]['item']['name']] = armorInfo['crafting']['materials'][i]['quantity']
    craftingMaterials = ''
    print('Crafting materials: ', end='')
    for item, quantity in materials.items():
        craftingMaterials += str(item) + " " + str(quantity) + "x, "
    print(craftingMaterials[:-2])
    print('\n')


if type == 'monsters':
    with open('D:\MHWDatabaseProject\MHWMonsters.txt') as storage:
        database = json.loads(storage.read())
    findMonster()
elif type == 'weapons':
    with open('D:\MHWDatabaseProject\MHWWeapons.txt') as storage:
        database = json.loads(storage.read())
    findWeapon()
elif type == 'armor':
    with open('D:\MHWDatabaseProject\MHWArmor.txt') as storage:
        database = json.loads(storage.read())
    findArmor()
