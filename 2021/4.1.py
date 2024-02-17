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
        word=word[0:len(word)-1]+instrukcje[i][1]
    elif instrukcje[i][0]=="USUN":
        word=word[0:len(word)-1]
    elif instrukcje[i][0]=="PRZESUN":
        letter=ord(instrukcje[i][1])+1
        if letter>90:
            letter-=26
        letter=chr(letter)
        index=word.index(instrukcje[i][1])
        if index==0:
            word=letter+word[index+1:len(word)]
        else:
            word=word[0:index]+letter+word[index+1:len(word)]

print(len(word))
file.close()