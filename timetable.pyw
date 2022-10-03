import datetime
import pyttsx3
import time
friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

def speak(audio):
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
h=[];m=[];data=[]; on_h=[];on_m=[];on_data=[]
speak("bạn muốn đặt bao nhiêu cuộc hẹn:")
x=input()
for y in range(0,int(x)):
      speak("Giờ hẹn giờ: ")
      h.append(input()+" ")
      speak("Phút hẹn trước:")
      m.append(input()+" ")
      speak("Nội dung cuộc hẹn:")
      data.append(input()+"#")

path_w = 'D:\SUNDAY\\testtime.txt'
with open(path_w, mode='w') as f:
    f.writelines(h)
    f.write('\n')
    f.writelines(m)
    f.write('\n')
    f.writelines(data)
with open('D:\SUNDAY\\testtime.txt', 'r',encoding='UTF-8') as f:
     datalist = f.readlines() 
     hour0 = (datalist[0])
     minute0=(datalist[1])
     sentence=datalist[2]
     f.close()
on_h=hour0.split()
on_m=minute0.split()
sentence=sentence.rstrip("#")
on_data=sentence.split("#")
print(on_h,on_m)
print(on_data)
n=0
#-------------------------------------------------------datetimes-----------------------------------------------
while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second
    for i in range(0,int(x)):
        if int(on_h[i]) == current_hour:
            if int(on_m[i]) == current_min:
                if current_sec==1:
                     print("Đã đến thời gian đã hẹn:"+on_data[i])
                     time.sleep(1)
                     n+=1
    if n>=int(x):
        exit()
                
          
                
      