import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os
import serial



friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

def speak(audio):
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
   
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("It is")
    speak(Time)

def welcome():
        #Chao hoi
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            speak("Good Morning Sir!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Sir!")
        elif hour>=18 and hour<24:
            speak("Good Evening sir")
        speak("How can I help you,boss") 


def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        print("Healer:")
        audio=c.listen(source,phrase_time_limit=5)
    try:
        query = c.recognize_google(audio,language='vi-VN')
        print("Healer -->: {}".format(query))
    except sr.UnknownValueError:
        query=""
    return query

if __name__  =="__main__":
    welcome()

    while True:
        query=command().lower()
        #All the command will store in lower case for easy recognition
        if query=="":
            print("...")
        elif "google" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        
        elif "youtube" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')

        elif "goodbye" in query:
            speak("Friday is off. Goodbye boss")
            quit()
        
        elif 'time' in query:
            time()
        elif "lên nhạc" in query:
            os.system("10minute.mp3")
 
        