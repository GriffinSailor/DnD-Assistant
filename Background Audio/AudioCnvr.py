
import os
from pydub import AudioSegment 

# Assign files 
cwd = os.getcwd()
input_file1 = cwd + '\Background Audio\Another One Bites The Dust.mp3'
output_file1 = cwd + '\Background Audio\Bites the Dust.wav'

input_file2 = cwd + "\Background Audio\Fat Bottomed Girls.mp3"
output_file2 = cwd + "\Background Audio\Fat Bottoms.wav"


input_file3 = cwd + "\Background Audio\Killer Queen.mp3"
output_file3 = cwd + "\Background Audio\Killer Q.wav"

print("\n\nall files assigned\n\n")
  
# Convert mp3s 
sound = AudioSegment.from_mp3(input_file1) 
print("first sound object was made")
sound.export(output_file1, format="wav") 
print("new file 1 made")

sound = AudioSegment.from_mp3(input_file2) 
sound.export(output_file2, format="wav") 
print("new file 2 made")

sound = AudioSegment.from_mp3(input_file3) 
sound.export(output_file3, format="wav") 