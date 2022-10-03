import pyttsx3
import speech_recognition as sr
import openpyxl
friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 
friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id)
def speak(audio):
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
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
#---------------------------------------------trochuyen---------------------------------------------------------
nhan=[] ; rep=[""]; 
wb = openpyxl.load_workbook('D:\\SUNDAY\\communication.xlsx')
noi=wb.sheetnames
print(noi)
mm=command().lower()
def trochuyen():
    n=2
    sheet=wb['Sheet1']
    while n<20:
        nhan.append("A"+ str(n))
        n+=1
    for t in range(2,19):
        rep.append(sheet[nhan[t]].value)
    m=0
    for x in range(2,20):
        if rep[t]!=None:
           if str(mm) in rep[t]:
             speak(""+sheet['B'+ str(t)].value)
trochuyen()