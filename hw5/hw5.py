#5 вариант
i = []
while True:
    a = input()
    if a == "":
        break
    if a[-1]=="r" and a[-2]=="u" and a[-3]=="t":
        i.append(a)
f = open("output.txt","w")
f.write("\n".join(i))
f.close()
