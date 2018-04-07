fin = open("mystem.xml", "r", encoding="utf-8")
text=fin.read()
fin.close()

b = text.find("<body>")
e = text.find("</body>")
r=len(text[b+len("<body>"):e])

fout = open("output1.txt", "w")
fout.write(str(r))
fout.close()
