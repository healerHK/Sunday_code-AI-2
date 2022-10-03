import webbrowser as wb
import pyautogui
import time
from sunday_action import speak
def onBoy_sunday():
    wb.open('http://192.168.1.18/')
    time.sleep(5)
    pyautogui.moveTo(660, 300)
    pyautogui.click()
    pyautogui.hotkey('Ctrl', 'w')
    speak("Clean_robot đã được mở")
def offBoy_sunday():   
    wb.open('http://192.168.1.18/')
    time.sleep(5)
    pyautogui.moveTo(660, 300)
    pyautogui.click()
    pyautogui.hotkey('Ctrl', 'w')
    speak("Clean_robot đã tắt")     
