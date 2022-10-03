from SUNDAY import SUNDAY
import speech_recognition as sr
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
while True:
    sunday=command().lower()
    if sunday=="":
        print('---')
    elif "sunday" in sunday:
        SUNDAY.welcome()
        SUNDAY.run_action()
    else: print("#3#3")
    