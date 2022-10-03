import wikipedia 
from googletrans import Translator
import  requests
from bs4 import BeautifulSoup
import pyttsx3
import re


friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

def speak(audio):
   print(audio)
   friday.say(audio)
   friday.runAndWait()   
def ALL_covid():
   text = "Đại dịch COVID-19 ở Việt Nam"
   wikipedia.set_lang("en")
   contents = wikipedia.summary(text).split('\n')
   Sum_covid=contents[0].split('.')
   trans=Translator()
   for i in range(1,3):
      text=trans.translate(Sum_covid[i],dest='vi')
      speak(text.text)

response = requests.get("https://covid19.gov.vn/big-story/cap-nhat-dien-bien-dich-covid-19-moi-nhat-hom-nay-171210901111435028.htm")
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.findAll( class_='kbwscwl-content clearfix',)
data=str(titles)
data_covid=data.replace('div class="kbwscwl-content clearfix">',"")
data_covid=data_covid.replace("</p><p>","")
data_covid=data_covid.replace("<<p>",'')
data_covid=data_covid.replace("</p></div>",'\n')
data_cv=data_covid.split("\n")
def Prov_covid():
   speak("Bạn muốn biết cô vít về tỉnh thành nào ?")
   cvid=input(); a=0 ; sum=0
   if cvid not in data:
         print("Không tìm thấy tình thành nào")
   else:
      for i in range(0,3):
         progress=data_cv[i].split(",")
         for j in progress:
               if cvid in j:
                  result=str(progress[a])
                  result=result.replace("Tính","")
                  speak(result) 
                  j=j.replace("(","có thêm ") 
                  j=j.replace(")", " ca mắc Cô Vít mới")   
                  speak(j)
                  N=re.findall(r'\d+', j)
                  sum=sum+int(N[0])

         a=1
      res="Tồng công 3 ngày qua tỉnh " + cvid +" đã có thêm "+str(sum)+" ca mắc mới"
      speak(res)
speak("Bạn muốn biết về Cô vít : tính hình chung , tình hình những ngày gần đây, tình hình của 1 tỉnh thành nào đó: ")
infor=input()
if "tình hình chung" in infor:
       ALL_covid()
elif "tình hình những ngày gần đây" in infor:
       
      for i in range(0,3):
            vn=data_cv[i].split(":")
            speak(vn[0].replace("Các tỉnh, thành phố ghi nhận ca bệnh như sau",""))
else : 
   Prov_covid()
