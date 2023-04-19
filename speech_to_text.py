import speech_recognition as sr
import pyttsx3

from transformers import pipeline
from transformers import AutoTokenizer, AutomaticSpeechRecognitionPipeline, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = "distilbert-base-uncased-finetuned-sst-2-english"


def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said : {text}")

    except:
        text = "Sorry couldn't not recognize your voice"

    print(text)
    return text


def sentiment():
    text_speech = pyttsx3.init()
    classifier = pipeline("sentiment-analysis", model="jonatasgrosman/wav2vec2-large-xlsr-53-english",
                          return_all_scores=True)

    result = classifier(speech_to_text())

    print(result)

    labels = result[0]
    pos = 0
    max =0
    for i in range(len(labels)):
        label = labels[i]
        if max < label['score']:
            max = label['score']
            pos = i

    print(result[0][pos]['score'])
    mood = result[0][pos]['label']

    text_speech.say(mood)

    text_speech.runAndWait()


# print(type(speech_to_text()))
sentiment()
