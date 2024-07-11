import MainMenu

def SelectAudio():
    selection = input("Select an Audio Type:\n(1)Background\n(2)Special Event\n(3)Return to Menu\n")
 
    # Input validation
    if not selection.isnumeric():
        print("\nIncorrect value type\n")
        SelectAudio()
    selection = int(selection)
    if selection > 3 or selection < 1:
        print("\nIncorrect value range\n")
        SelectAudio()
    
    # Background Audio selected
    if selection == 1:
        print("\nBackground Audio Selected!\n")
        SelectAudio()

    # Special Event Audio selected
    if selection == 2:
        print("\nSpecial Event Audio Selected!\n")
        SelectAudio()

    # Return to main menu
    if selection == 3:
        print("\n")
        MainMenu.PrintMenu()