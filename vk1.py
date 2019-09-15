
""" Making an assistant like siri,ok google,alexa etc. using the python3"""   
#module used to convert text into speech
import pyttsx3

#module to get the current date and time
import datetime

#Python supports many speech recognition engines and APIs, including Google Speech Engine
import speech_recognition as sr


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


if __name__== "__main__":
    wishMe()
