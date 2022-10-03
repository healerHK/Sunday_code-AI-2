import pyttsx3
import time
import os
import pyautogui
import openpyxl
import random

friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id)

def speak(audio):
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def funny_story():
 wb = openpyxl.load_workbook('D:\haha.xlsx')
 desease=wb.sheetnames
 sheet = wb['Sheet1']
 list=range(1,20); funny=range(2,5)
 number="A"+str(random.choice(list))
 cell= sheet[number]
 speak(cell.value)
 link='D:\\funny\\'+str(random.choice(funny))+'.mp3'
 print(link)
 os.startfile(link)
 time.sleep(5)
 pyautogui.keyDown('Alt')
 pyautogui.press('F4')
 pyautogui.keyUp('Alt')




