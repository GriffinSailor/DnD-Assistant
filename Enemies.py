import MainMenu

def SelectEnemy():
    selection = int(input("Select an Enemy to Spawn:\n(1)Common Enemy\n(2)Rare Enemy\n(3)Epic Enemy\n(4)Return to Menu\n"))
 
    # Input validation
    if type(selection) != int:
        print("\nIncorrect value type\n")
        SelectEnemy()
    if selection > 4 or selection < 1:
        print("\nincorrect value range\n")
        SelectEnemy()
    
    # Common Enemies selected
    if selection == 1:
        print("Common Enemies Selected!\n")
        SelectEnemy()

    # Rare Enemies selected
    if selection == 2:
        print("Rare Enemies Selected!\n")
        SelectEnemy()

    # Epic Enemies selected
    if selection == 3:
        print("Epic Enemies Selected!\n")
        SelectEnemy()

    # Return to main menu
    if selection == 4:
        print("\n")
        MainMenu.PrintMenu()