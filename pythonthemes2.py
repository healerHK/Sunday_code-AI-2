from tkinter import * as Tk
import time
import os
import tkinter
from tkinter.font import Font
from typing import Sized
import test2
import threading
from SUNDAY import SUNDAY
import re


root = Tk()
root.iconbitmap('D:\SUNDAY\\sunday_main1.ico')
text= Text(root,width=35,height=10, bg="black", fg='white',font=('Future Worlds',16))


root.title("    S.U.N.D.A.Y")
root.geometry("500x670")
root.configure(background="black")
 
frameCnt = 100
frames = [PhotoImage(file='C:\\Users\HealerHK\Desktop\sunday2.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
label2 = Label(master=frames, text="S.U.N.D.A.Y: (75, 75)", bg="yellow",Font=("Impact",18))
label2.place(x=75, y=75)
def update(ind):
    
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(80, update, ind)

label = Label(root, bg='black')
label.pack()
root.after(0, update, 0)

text.place(x=65, y=550)
def add_text():
    n=1
    text1=['text20']
    with open('D:\SUNDAY\\textt.txt', mode='r',encoding='UTF-8') as f:
        text1[0]=f.read()
        f.close()
    while True:
        text1.append("text2"+str(n))
        with open('D:\SUNDAY\\textt.txt', mode='r',encoding='UTF-8') as f:
            text1[n]=f.read()
            f.close()
        if text1[n]!=text1[n-1]:
            t=text1[n].split('\n')
            text.delete("1.0","end")
            for i in t:
                i=i.strip()
                text.tag_configure("tag_name", justify='center')
                text.insert('1.0', i)
                text.tag_add("tag_name", "1.0", "end")
                text.pack()

                m1 = re.findall(r'\d', i)
                t=len(i.split())/5 +len(m1)/5.9
                time.sleep(t)
                text.delete("1.0","end")
       
        n+=1
        time.sleep(0.5)


run=SUNDAY.run_action
thread = threading.Thread(target=run)
thread.daemon = True 
thread.start()
thread1=threading.Thread(target=add_text)
thread1.daemon=True
thread1.start()

root.mainloop()

