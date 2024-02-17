
file=open("instrukcje.txt", "r")
letters=[]
word=""
for line in file:
    line=line.rstrip()
    temp=line.split(" ")
    if temp[0]=="DOPISZ":
        letters.append(temp[1])

file.close()

dict={}
for char in set(letters):
    dict[char]=letters.count(char)

print(dict)
print(dict["Z"])

