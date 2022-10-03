import time
with open("valungtung.txt", 'r') as F:
    n=F.read()
    F.close()
print(n)
time.sleep(1)
with open("valungtung2.txt", 'r') as k:
    m=k.read()
    k.close()
print(m)