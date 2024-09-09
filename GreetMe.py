import pyttsx3
import datetime

engine = pyttsx3.init("sapi5") 
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) 
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def greetMe():
    current_time = datetime.datetime.now()

    if 0 <= current_time.hour < 12:
        greeting = "Good morning Ma'am! How may I assist you today?"
    elif 12 <= current_time.hour < 18:
        greeting = "Good afternoon Ma'am! What would you like to do today?"
    else:
        greeting = "Good evening Ma'am! It's a pleasure to see you again."

    speak(greeting)