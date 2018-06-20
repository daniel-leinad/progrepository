import re
import os
def func(filename, tablitsa):
    #otkryvaem fayl
    f=open("news/"+filename+".html", "r", encoding="utf-8")
    text=f.read()
    f.close()
    #berem vse slovoformy
    matches = re.findall(r'<w><ana lex="(\w+)" gr=".+"></ana>.+</w>', text)
    #zapisyvaem v tablitsu tolko te kotorye nachinautsya na zaglavnuyu bukvu
    for match in matches:
        if match[0].isupper() and match[0].isalpha():
            if match in tablitsa:
                tablitsa[match]+=1
            else:
                tablitsa[match]=1
    return tablitsa
s={}
#telo programmy
lod = os.listdir(path="news/")
for file in lod:
    s=func(file[:-5], s)
#zapis v fayl
f1 = open("names.csv", "w", encoding="utf-8")
for i in s:
    f1.write(i+"\t"+str(s[i])+"\n")
f1.close()
