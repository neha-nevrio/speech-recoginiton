import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

# initializing pyttsx3
text_speech = pyttsx3.init()

# Function to convert speech to text:
with sr.Microphone() as source:
    print("Say Something...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text_speech.say(f"Did you say {text}")

    except:
        text_speech.say("Sorry couldn't not recognize your voice")

    finally:
        text_speech.runAndWait()
