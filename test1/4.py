f = open("Ozhegov.txt", "r", encoding="utf8")
s = f.read()
s=s.split("\n")
f.close()
l=[]
while True:
    w = input().lower()
    if w == "":
        break
    else:
        l.append(w)
#выводим инфу по каждому слову
for word in l:
    #ищем слово
    found = False
    for string in s:
        if string[:len(word)]==word:
            found=True
            break
    if found:
        string=string.split("|")
        print(string[0]+" - "+string[3]+" - "+string[1])
    else:
        print("такое слово не нашлось")
