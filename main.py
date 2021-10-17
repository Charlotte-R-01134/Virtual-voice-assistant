import wolframalpha
import pyttsx3
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import ctypes
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def intro():
    print(""" _________        .---\"""      \"""---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  J a r v i s   | |             
|:______B:|      | |                | |             
|:______B:|      | |                | |             
|         |      | |                | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:""")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        print("Me: Good morning")
        speak("Good morning")
    
    elif hour >= 12 and hour < 18:
        print("Me: Good afternoon")
        speak("Good afternoon")

    else:
        print("Me: Good evening")
        speak("Good Evening")

    print(f"I am your assistant, jarvis")
    speak(f"I am your assistant, jarvis")
    speak("How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Thinking...")
        query = r.recognize_google(audio, language='en')
        print(f"You: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to recognize your voice")
        return "None"
    
    return query

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    intro()

    while True:
        query = takeCommand().lower()

        if 'good morning' in query:
            print("Me: Good morning")
            speak("Good morning")
            print(f"Me: How are you")
            speak(f"How are you")

        elif 'good afternoon' in query:
            print("Me: Good afternoon")
            speak("Good afternoon")
            print(f"Me: How are you")
            speak(f"How are you")

        elif 'good evening' in query:
            print("Me: Good Evening")
            speak("Good Evening")
            print(f"Me: How are you")
            speak(f"How are you")

        elif 'wikipedia' in query:
            print("Me: searching wikipedia")
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print("Me: According to wikipedia")
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Me: Opening youtube")
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            print("Me: Opening google")
            speak("Opening google")
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            print("Me: Opening stack over flow")
            speak("Opening stack over flow")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or 'play song' in query:
            print("Me: Opening music")
            speak("Opening music")
            music_dir = r"C:\Users\cemil\Music\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query or 'what is the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Me: It is {time}")
            speak(f"It is {time}")

        elif 'open word' in query:
            print("me: opening word")
            speak("Opening word")
            codePath = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(codePath)

        elif 'how are you' in query:
            print("Me: I am fine, thank you")
            speak("I am fine, thank you")
            print("Me: how are you?")
            speak("How are you?")
        
        elif 'fine' in query or 'good' in query:
            print("Me: I am glad")
            speak("I am glad")

        elif 'bad' in query or 'sad' in query:
            print("Me: i am sorry too hear that")
            speak("I am sorry to hear that")

        elif "what's your name" in query or 'who are you' in query:
            print(f"My friends call me jarvis")
            speak(f"My friends call me jarvis")

        elif 'exit' in query or 'sleep' in query or 'goodbye' in query:
            print("Me: Have a nice day")
            speak("Have a nice day")
            exit()

        elif 'who made you' in query or 'who created you' in query:
            print("Me: I was made by Charlotte")
            speak("I was made by Charlotte")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(f"Me: {joke}")
            speak(joke)

        elif 'calculate' in query:
            appid = "UK4TWX-7UT68X5X77"
            client = wolframalpha.Client(appid)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print(f"Me: The answer is {answer}")
            speak(f"The answer is {answer}")

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'who am i' in query:
            print("Me: Most definitely human")
            speak("Most definitely human")
        
        elif 'what is the meaning of life' in query:
            print("Me: 42")
            speak("42")

        elif 'what is love' in query:
            print("Me: It is the 7th sense that destroys all other senses")
            speak("It is the 7th sense that destroys all other senses")

        elif 'who are you' in query:
            print("Me: I am your virtual assistant")
            speak("I am your virtual assistant")

        elif 'lock window' in query:
            print("Me: locking device")
            speak("Locking device")
            ctypes.windll.user32.LockWorkStation()

        elif 'where is' in query:
            qury = query.replace("where is", "")
            location = query
            print(f"Me: Locating {location}")
            speak(f"Locating {location}")
            webbrowser.open(f"https://www.google.nl/maps/place/{location}")

        elif 'jarvis' in query:
            print(f"Me: Jarvis 1 point o at your service, jarvis")
            speak(f"Jarvis 1 point o at your service, jarvis")           

        elif 'what is' in query or 'who is' in query:
            appid = "UK4TWX-7UT68X5X77"
            client = wolframalpha.Client(appid)
            res = client.query(query)

        else:
            print("Me: No results, would you like me to look on the web for you?")
            speak("No results, would you like be to look on the web for you?")
            request = takeCommand()
            if "yes" in str(request) or "yeah" in str(request) or "yep" in str(request):
                webbrowser.open(query)