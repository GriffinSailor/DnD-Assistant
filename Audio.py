import MainMenu
from playsound import playsound
import multiprocessing

def SelectAudio():
    selection = input("Select an Audio Type:\n(1)Background\n(2)Special Event\n(3)End Music\n(4)Return to Menu\n")
 
    # Input validation
    if not selection.isnumeric():
        print("\nIncorrect value type\n")
        SelectAudio()
    selection = int(selection)
    if selection > 4 or selection < 1:
        print("\nIncorrect value range\n")
        SelectAudio()
    
    # Background Audio selected
    if selection == 1:
        print("\nBackground Audio Selected!\n\n")
        #playsound('Background Audio/Another One Bites The Dust.mp3', False)

        # player = multiprocessing.Process(target = playsound, args = ("Background Audio/Another One Bites The Dust.mp3",))
        # player.start()
        # input("press ENTER to stop playback")
        #multiprocessing.player.terminate()
        
        SelectAudio()

    # Special Event Audio selected
    if selection == 2:
        print("\nSpecial Event Audio Selected!\n")
        SelectAudio()

    if selection == 3:
        print("\nShutting Down Audio!\n")
        playsound('Background Audio/Silence.mp3', False)
        SelectAudio()

    # Return to main menu
    if selection == 4:
        print("\n")
        MainMenu.PrintMenu()