from datetime import datetime
import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour >=12 and hour <18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I'm jarvis sir, How can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query} \n")
    
    except Exception as e:
        print("Say that again please")
        return "None"
    return query
if __name__ == "___main__":
    wishMe()
    # speak("Siam is google software")
    takeCommand()
# row,coloumn = map(int,input().split())
# for i in range(1,row,2):
#     print((i*".|.").center(coloumn,'-'))
# print('WELCOME'.center(coloumn,"-"))
# for i in range(row-2,-1,-2):
#     print((i*".|.").center(coloumn,'-'))