import pyttsx3

text_speech = pyttsx3.init()

text = input("Write something here to listen - ")

text_speech.say(text)

text_speech.runAndWait()

