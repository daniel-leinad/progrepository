import re

fin = open("mystem.xml", "r", encoding="utf-8")
text=fin.read()
fin.close()

r=re.findall('gr="(.+)"', text)
dictionary={}
for i in r:
    dictionary[i]=0
for i in r:
    dictionary[i]+=1
res = []
for i in dictionary:
    res.append([dictionary[i],i])
res.sort(reverse=True)

fout = open("output2.txt", "w")
for i in res:
    fout.write(i[1]+"\n")
fout.close()
