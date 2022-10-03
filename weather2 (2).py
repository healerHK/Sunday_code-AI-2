import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import threading
import time

friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

with open('D:\SUNDAY\\textttt.txt', mode='r',encoding='UTF-8') as f:
        text1=f.read()
        f.close()
t=text1.split('.')

def speak(audio):
    with open('D:\SUNDAY\\textt.txt', mode='w',encoding='UTF-8') as f:
        f.write(audio)
    friday.say(audio)
    friday.runAndWait()
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        print("Healer:")
        audio=c.listen(source,phrase_time_limit=3)
    try:
        sunday = c.recognize_google(audio,language='vi-VN')
        print("Healer -->: {}".format(sunday))
    except sr.UnknownValueError:
        sunday=""
    return sunday

def stop():
    while True:
        m=command().lower()
        if "dừng" in m or "thôi" in m:
            with open ("D:\SUNDAY\Stop.txt", mode='w', encoding='UTF-8') as f:
                f.write("dừng lại")
            break
        
def run():
    while True:
        for i in t:
            with open ("D:\SUNDAY\Stop.txt", mode='r', encoding='UTF-8') as f:
                choose=f.read()
                open("D:\SUNDAY\Stop.txt", "w").close()
            if "dừng lại" in choose:
                    exit()
            else:
                    speak(i)
thread1 = threading.Thread(target=stop)
thread1.start()                
run()

    


    

    
            

        
    
         

     



