import MainMenu
import csv

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
        SpawnCommon()
        SelectEnemy()

    # Rare Enemies selected
    if selection == 2:
        SpawnRare()
        SelectEnemy()

    # Epic Enemies selected
    if selection == 3:
        SpawnEpic()
        SelectEnemy()

    # Return to main menu
    if selection == 4:
        print("\n")
        MainMenu.PrintMenu()

# CSV layout:
# rarity,name,hp,strength,dexterity,intellect,constitution,wisdom,charisma,inventory,special abilities

def SpawnCommon():
    file = open("Enemies.csv", "r")
    reader = csv.reader(file, delimiter = ',')
    readerValues = []
    for row in reader:
        if row[0] == 'Common':
            readerValues.append(row)
    
    # Printing the stats of the chosen enemy
    chosen = readerValues[0]
    print("\n~Common Enemy~\n\n")
    print(chosen[1])
    print(chosen[2] + " HP")
    print("Str: " + chosen[3] + "           Dex: " + chosen[4] + "\nInt: " + chosen[5] + "           Cons: " + chosen[6] + "\nWis: " + chosen[7] + "           Char: " + chosen[8])
    print("Inventory: " + chosen[9])
    print("Special Ability: " + chosen[10] + "\n\n")

def SpawnRare():
    file = open("Enemies.csv", "r")
    reader = csv.reader(file, delimiter = ',')
    readerValues = []
    for row in reader:
        if row[0] == 'Rare':
            readerValues.append(row)

    # Printing the stats of the chosen enemy
    chosen = readerValues[0]
    print("\n~Common Enemy~\n\n")
    print(chosen[1])
    print(chosen[2] + " HP")
    print("Str: " + chosen[3] + "           Dex: " + chosen[4] + "\nInt: " + chosen[5] + "           Cons: " + chosen[6] + "\nWis: " + chosen[7] + "           Char: " + chosen[8])
    print("Inventory: " + chosen[9])
    print("Special Ability: " + chosen[10] + "\n\n")

def SpawnEpic():
    file = open("Enemies.csv", "r")
    reader = csv.reader(file, delimiter = ',')
    readerValues = []
    for row in reader:
        if row[0] == 'Epic':
            readerValues.append(row)

    # Printing the stats of the chosen enemy
    chosen = readerValues[0]
    print("\n~Common Enemy~\n\n")
    print(chosen[1])
    print(chosen[2] + " HP")
    print("Str: " + chosen[3] + "           Dex: " + chosen[4] + "\nInt: " + chosen[5] + "           Cons: " + chosen[6] + "\nWis: " + chosen[7] + "           Char: " + chosen[8])
    print("Inventory: " + chosen[9])
    print("Special Ability: " + chosen[10] + "\n\n")