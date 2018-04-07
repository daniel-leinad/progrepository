import re

fin = open("mystem.xml", "r", encoding="utf-8")
text=fin.read()
fin.close()

r=re.findall(r'<w><ana lex="(\w+)" gr="(.*)" />(\w+)</w>', text)
for i in r:
    print(",".join(i))

fout = open("output32.txt", "w")
for i in r:
    fout.write(",".join(i)+"\n")
fout.close()

