import MainMenu
import csv
import random

def SelectEnemy():
    selection = input("Select an Enemy to Spawn:\n(1)Common Enemy\n(2)Rare Enemy\n(3)Epic Enemy\n(4)Return to Menu\n")
 
    # Input validation
    if not selection.isnumeric():
        print("\nIncorrect value type\n")
        SelectEnemy()
    selection = int(selection)
    if selection > 4 or selection < 1:
        print("\nIncorrect value range\n")
        SelectEnemy()
    
    # Common Enemies selected
    if selection == 1:
        SpawnEnemy(selection)
        SelectEnemy()

    # Rare Enemies selected
    if selection == 2:
        SpawnEnemy(selection)
        SelectEnemy()

    # Epic Enemies selected
    if selection == 3:
        SpawnEnemy(selection)
        SelectEnemy()

    # Return to main menu
    if selection == 4:
        print("\n")
        MainMenu.PrintMenu()

# CSV layout:
# 0-rarity,1-name,2-minHP,3-maxHP,4-minStrength,5-maxStrength,6-minDexterity,7-maxDexterity,8-minIntellect,9-maxIntellect,10-minConstitution,
# 11-maxConstitution,12-minWisdom,13-maxWisdom,14-minCharisma,15-maxCharisma,inventory,special abilities

def SpawnEnemy(rarity):
    file = open("Enemies.csv", "r")
    reader = csv.reader(file, delimiter = ',')
    readerValues = []

    # Filling proper rarity enemy options
    if rarity == 1:
        for row in reader:
            if row[0] == 'Common':
                readerValues.append(row)
        print("\n~Common Enemy~\n\n")
    elif rarity == 2:
        for row in reader:
            if row[0] == 'Rare':
                readerValues.append(row)
        print("\n~Rare Enemy~\n\n")
    elif rarity == 3:
        for row in reader:
            if row[0] == 'Epic':
                readerValues.append(row)
        print("\n~Epic Enemy~\n\n")
    
    # Choosing the enemy
    chosen = random.choice(readerValues)

    # Randomly generating the stats of the enemy
    health = random.randrange(int(chosen[2]), int(chosen[3]))
    strength = random.randrange(int(chosen[4]), int(chosen[5]))
    dexterity = random.randrange(int(chosen[6]), int(chosen[7]))
    intellect = random.randrange(int(chosen[8]), int(chosen[9]))
    constitution = random.randrange(int(chosen[10]), int(chosen[11]))
    wisdom = random.randrange(int(chosen[12]), int(chosen[13]))
    charisma = random.randrange(int(chosen[14]), int(chosen[15]))

    # Printing the stats of the chosen enemy
    print(chosen[1])
    print(str(health) + " HP")
    print("Str: " + str(strength) + "           Dex: " + str(dexterity) + "\nInt: " + str(intellect) + "           Cons: " + 
          str(constitution) + "\nWis: " + str(wisdom) + "           Char: " + str(charisma))
    print("Inventory: " + chosen[9])
    print("Special Ability: " + chosen[10] + "\n\n")