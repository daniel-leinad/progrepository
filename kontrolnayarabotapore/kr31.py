import re

fin = open("mystem.xml", "r", encoding="utf-8")
text=fin.read()
fin.close()

r=re.findall('gr="(.*мн.*,сов.*|.*,сов.*мн.*|сов.*мн.*)"', text)
fout = open("output31.txt", "w")
fout.write(str(len(r)))
fout.close()
