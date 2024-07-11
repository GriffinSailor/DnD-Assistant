import MainMenu

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

def SpawnCommon():
    print("\n~Common Enemy~\n\n")
    print("Jimmy the Weakling")
    print("100 HP")
    print("Str: 7           Dex: 9\nInt: 7           Cons: 7\nWis: 7           Char: 7")
    print("Inventory: Kitchen knife")
    print("Special Ability: Scream and Shout\n\n")

def SpawnRare():
    print("\n~Rare Enemy~\n\n")
    print("Jimmy the Strong")
    print("150 HP")
    print("Str: 10           Dex: 10\nInt: 10           Cons: 10\nWis: 10           Char: 10")
    print("Inventory: Worn down pistol")
    print("Special Ability: Rally Allies\n\n")

def SpawnEpic():
    print("\n~Epic Enemy~\n\n")
    print("Jimmy the Grand")
    print("300 HP")
    print("Str: 15           Dex: 15\nInt: 15           Cons: 15\nWis: 15           Char: 15")
    print("Inventory: Cool Blade")
    print("Special Ability: Call on the abyss\n\n")