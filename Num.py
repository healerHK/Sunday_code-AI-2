from typing import TYPE_CHECKING
import numpy as np
mm=[]; Per=[];sentence=0
St_main="Bạn có thể giúp gì cho tôi"
for j in range(0,3):
     print("Nhập câu Ai:")
     m=input()
     mm.append(m)
for h in mm:
    n=0
    st=h.split()
    St_mains=St_main.split()
    for i in st:
         if i in St_main.lower():
             n+=1
    Persent= (n/len(St_mains))*100
    Per.append(round(Persent,2))
Max=max(Per)
print(Max)
for i in range (0,len(Per)):
    if Per[i]== Max:
        print(mm[i])
    
    