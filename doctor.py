import pyttsx3
import speech_recognition as sr
import os
import openpyxl
import pprint
import time
import datetime
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
#-------------------------------------------------------timbenh----------------------------------------------------------
def Find_desease():
    n=2
    sheet=wb['Sheet1']
    while n<50:
        cell.append("C"+ str(n))
        n+=1
    for x in range(0,48):
        
        low=sheet[cell[x]].value
        da.append(low.lower())
        
    m=0
    for x in range(0,49):
        if da[x]!=None:
           if str(haha) in da[x]:
              print("_______________________________________________________________________________\n")
              speak("-Tên bệnh: "+sheet['B'+ str(x+1)].value)
              print("_______________________________________________________________________________\n")
              #print("-Triệu chứng : "+sheet['C'+ str(x+1)].value)
              #print("_______________________________________________________________________________\n")
              #print("-Phương pháp điều trị:  "+sheet['D'+ str(x+1)].value)
              #print("_______________________________________________________________________________\n")
cell=[] ; da=[""]; 
wb = openpyxl.load_workbook('D:\\SUNDAY\\doctor.xlsx')
desease=wb.sheetnames
speak('Triệu chứng của bạn là gì:')
haha=input().lower()       
Find_desease()




        
    
         

     



