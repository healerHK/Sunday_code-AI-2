from datetime import datetime
with open('D:\SUNDAY\Face_detect\Attendance.csv','r+') as f:
    myDataList = f.readlines()
    print(myDataList)
    nameList = []; timelist=[]; time=[]
    for line in myDataList:
        entry = line.split(',')
        nameList.append(entry[0])
        timelist.append(entry[1])
        for i in timelist:
            i=i.replace('\n',"")
            time.append(i)
print(time)
now = datetime.now()
dtString = now.strftime('%H:%M')
with open('D:\SUNDAY\Face_detect\Attendance.csv','r+') as f:
    if dtString not in time:
        f.writelines(f'\n{dtString}\n')
print(dtString)
print(type(dtString))