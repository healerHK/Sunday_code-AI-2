import threading
import time
from tkinter.constants import TRUE
def run():
    i =10
    while i<20:
        print(i)
        i+=1
def add_text():
    j=1
    while True:
        print(j);
        j+=1
        time.sleep(2)
thread = threading.Thread(target=run)
thread.start()
thread1=threading.Thread(target=add_text)
thread1.start()