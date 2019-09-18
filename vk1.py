
""" Making an assistant like siri,ok google,alexa etc. using the python3"""   
#module used to convert text into speech
import pyttsx3

#module to get the current date and time
import datetime

#module used to activate some of the some functions of the webbrowser
import webbrowser

#Python supports many speech recognition engines and APIs, including Google Speech Engine
import speech_recognition as sr

#module used to get an informaton from the wikipedia
import wikipedia

#module allows us to handle various operations regarding time, its conversions and representation
import time 

#initailizing the module which convert text to speech
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-50)
#print(voices[16].id)  (used to check which voices are available in the system)

#speak function speaks the text given to it
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wishMe function wishes the user according to time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Eveninng")
    speak("Hello i am vk's Assitant How may i help you")

#this function takes the speech as input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query.lower()}\n")
    except Excepton as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query


if __name__== "__main__":
    wishMe()
    count=1 # count takes the number of command
    while(count!=0):
        query = takeCommand().lower()
        print(f"User said:{query}\n")

        #logic for executing commands

        
        #for searching wikipedia
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results) 
            speak(results)
            
        #tell me about Time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
            
        #for opening websites like youtube,google,codeforces etc.  
        elif 'open youtube'in query:
            webbrowser.open_new_tab("https://www.youtube.com/")
            speak("youtube opened")
            print("youtube opened")
        elif 'open google'in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("google opened")
            print("google opened")
        elif 'open codeforces'in query:
            webbrowser.open_new_tab("https://www.codeforces.com/")
            speak("codeforces opened")
            print("codeforces opened")


        count=count-1
