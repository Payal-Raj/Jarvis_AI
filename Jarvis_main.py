import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5") 
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) 
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 
        r.energy_threshold = 300 
        audio = r.listen(source,0,4) 
         
        try:
            print("Understanding....")
            query = r.recognize_google(audio,language='en-in')
            print(f"You Said:  {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

        while True:
            query = takeCommand().lower()
            if "go to sleep" in query:
                speak("Alright. Feel free to call me whenever you need assistance.")
                break 

            elif "hello" in query:
                speak("Hey there! How are you?")
            elif "i am good" in query:
                speak("That's great to hear!")
            elif "thank you" in query:
                speak("Don't mention it. I'm just doing my job as your friendly AI assistant.")
            