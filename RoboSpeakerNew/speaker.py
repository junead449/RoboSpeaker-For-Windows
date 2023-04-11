from gtts import gTTS
import os
mytext =" "
while mytext != 'quit':
    mytext = input("This is a Robotic System: Not a Human or Real System ")
    audio = gTTS(text=mytext, lang="en", slow=False)

    audio.save("example.mp3")
    os.system("start example.mp3")


