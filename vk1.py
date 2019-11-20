
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
# Source function for the news command
#uses the api of the times of india for fetching the news
def Parsefeed():
    f = feedparser.parse("http://timesofindia.indiatimes.com/rssfeedstopstories.cms")
    ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init('News Notify')

    for newsitem in f['items']:
        n = notify2.Notification(newsitem['title'], newsitem['summary'], icon=ICON_PATH)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.show()
        n.set_timeout(15)
        #time.sleep(5)
        print(newsitem['title'])
        speak(newsitem['title'])
        print(newsitem['summary'])
        speak(newsitem['summary'])
        print('\n')
    speak("That's all for today")

# source function for the weather news
# uses the api of the openweathermap site for fetching the weather report  
def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
		speak("Apke sahar" + name+"main mausam kuch iss prakar hai" )
		speak("It's all "+desc+"in the sky" )
		speak("Tapman degree fahrenheit mai")
		speak(temp)
		
		
	except:
		final_str = 'There was a problem retrieving that information'
def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	format_response(weather)



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
        
        #play music on youtube
        elif 'play saki saki'in query:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=-m_WlHjFvPE&list=RDMM-m_WlHjFvPE&start_radio=1")
        
        #play music from folder
        elif 'play music'in query:
            
            music_dir = "//home//vishnu//Music"
            songs = os.listdir(music_dir)
            print(songs[1])
            webbrowser.open(os.path.join(music_dir,songs[1]))
        
        #Aj ke samaachar
        elif "today's news" in query:
            try:
                Parsefeed()
            except:
                print("Error")
        #weather report
        elif "today's weather" in query:
            get_weather("lucknow")
        # not at home
        elif "where is vishnu" in query:
            #tellinfo();
            speak(message)
        elif "record message" in query:
            message=query[14:]
            print(message)
            #speak(smessage)
        count=count-1
