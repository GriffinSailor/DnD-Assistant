import MainMenu
import simpleaudio as sa

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


        wave_object = sa.WaveObject.from_wave_file('C:/Users/john/OneDrive/Desktop/DnD Assistant/Background Audio/Another One Bites The Dust.wav')
        print('playing sound using simpleaudio')

        # define an object to control the play
        play_object = wave_object.play()
        play_object.wait_done()



        SelectAudio()

    # Special Event Audio selected
    if selection == 2:
        print("\nSpecial Event Audio Selected!\n")
        SelectAudio()

    if selection == 3:
        print("\nShutting Down Audio!\n")
        SelectAudio()

    # Return to main menu
    if selection == 4:
        print("\n")
        MainMenu.PrintMenu()