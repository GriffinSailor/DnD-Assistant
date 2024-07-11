import Enemies

def PrintMenu():
    selection = int(input("Main Menu:\n(1)Select Enemies\n(2)Music Control\n(3)End Session\n"))
 
    # Input validation
    if type(selection) != int:
        print("\nIncorrect value type\n")
        PrintMenu()
    if selection > 3 or selection < 1:
        print("\nincorrect value range\n")
        PrintMenu()
    
    # Enemies screen selected
    if selection == 1:
        print("Enemies Selected!\n")
        Enemies.SelectEnemy()

    # Music screen selected
    if selection == 2:
        print("Music Selected!\n")
        PrintMenu()

    # End session selected
    if selection == 3:
        exitVer = input("\nAre you sure? Your progress will be saved. (Y/N)\n")

        # Input Validation
        if exitVer.upper() == "Y":
            return 1
        else:
            print("\nDid not end session\n")
            PrintMenu()