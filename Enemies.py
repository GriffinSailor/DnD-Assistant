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
        print("\nRare Enemies Selected!\n")
        SelectEnemy()

    # Epic Enemies selected
    if selection == 3:
        print("\nEpic Enemies Selected!\n")
        SelectEnemy()

    # Return to main menu
    if selection == 4:
        print("\n")
        MainMenu.PrintMenu()

def SpawnCommon():
    print("\n~Common Enemy~\n\n")
    print("Jimmy the Weakling")
    print("Vit: 9           Str: 9\nDex: 9           Int: 9\nWis: 9           Pop: 9")
    print("Inventory: Common knife")
    print("Special Ability: Shadow Bust\n\n")