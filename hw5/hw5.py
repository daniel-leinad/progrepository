#5 вариан
#вводим список
i = []
#считываем слова
while True:
    a = input()
    if a == "":
        break
    #проверяем, оканчивается ли слово на tur, если да, то добавляем его в список
    if a[-1]=="r" and a[-2]=="u" and a[-3]=="t":
        i.append(a)
#записываем список в файл
f = open("output.txt","w")
f.write("\n".join(i))
f.close()
