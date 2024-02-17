file=open("instrukcje.txt", "r")
instrukcje=[]
word=""
for line in file:
    line=line.rstrip()
    temp=line.split(" ")
    instrukcje.append(temp[0])
file.close()
dopiszMax=0
zmienMax=0
usunMax=0
przesunMax=0
counter=0
last=instrukcje[0]
for i in range(1,len(instrukcje)):
    if instrukcje[i]==last:
        counter+=1
    else:
        if last=="DOPISZ":
            if counter>dopiszMax:
                dopiszMax=counter
        elif last=="ZMIEN":
            if counter>zmienMax:
                zmienMax=counter
        elif last=="USUN":
            if counter>usunMax:
                usunMax=counter
        elif last=="PRZESUN":
            if counter>przesunMax:
                przesunMax=counter
        counter=1
    last=instrukcje[i]

print(dopiszMax)
print(zmienMax)
print(usunMax)
print(przesunMax)

