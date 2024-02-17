file=open("instrukcje.txt", "r")
instrukcje=[]
word=""
for line in file:
    line=line.rstrip()
    temp=line.split(" ")
    instrukcje.append(temp)

for i in range(0,len(instrukcje)):
    if instrukcje[i][0]=="DOPISZ":
        word+=instrukcje[i][1]
    elif instrukcje[i][0]=="ZMIEN":
        word=word.rstrip(word[-1])
        word+=instrukcje[i][1]
    elif instrukcje[i][0]=="USUN":
        word=word.rstrip(word[-1])
    elif instrukcje[i][0]=="PRZESUN":
        for j in range(0,len(word)):
            if word[j]==instrukcje[i][1]:
                char=(word[j])
                if word[j]=="Z":
                    word.replace(instrukcje[i][1],"A",1)
                else:
                    word.replace(char,str(chr((ord(char) + 1-65) % 26 + 65)),1)

print(len(word))
file.close()