import re
import os
def func(filename):
    f=open("news/"+filename+".html", "r", encoding="utf-8")
    text=f.readlines()
    f.close()
    finaltext=""
    #Dalee ubiraem vse tegi i izbavlayemsya ot udareniy i lishnih probelov
    tag=False
    for line in text:
        #berem tolko strochki gde est slova
        if line[:3]=="<w>":
            for i in range(len(line)):
                if line[i] == "<" and not tag:
                    tag=True
                elif line[i] == ">" and tag:
                    tag=False
                #Ubiraem vse tegi i izbavlayemsya ot udareniy i lishnih probelov
                elif line[i]!="\n" and line[i]!="`" and not (line[i]==" " and (line[i+1]=="." or line[i+1]=="," or line[i+1]=="!" or line[i+1]=="?")) and not tag:
                    finaltext+=line[i]
            if finaltext[-1]!=" ":
                finaltext+=" "
        if line[-5:-1]=="</p>":
            finaltext+="\n"
    #dobavlayem nazvanie v nachalo finaltext
    title = re.search(r"<title>(.+)</title>", "\n".join(text))
    t=[]
    t.append(str(title.group(1)))
    t.append(finaltext)
    res="\n".join(t)
    #zapisyvaem eto vse v fayl
    f2 = open(filename+".txt", "w", encoding="cp1251")
    f2.write(res)
    f2.close()
#telo programmy
lod = os.listdir(path="news/")
for file in lod:
    func(file[:-5])
