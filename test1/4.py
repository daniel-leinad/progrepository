f = open("Ozhegov.txt", "r", encoding="utf8")
s = f.read()
s=s.split("\n")
f.close()

l=[]
#вводим слова в l
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
    for i in s:
        a=i.split("|")
        if a[0]==word:
            found=True
            break
    if found:
        print(a[0]+" - "+a[3]+" - "+a[1])
    else:
        print("такое слово не нашлось")
