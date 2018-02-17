#5 variant

from random import choice

#sozdaem massiv i slovar
words = []
hints = {}
#otkryvaem fayl i zagruzhaem iz nego dannye v massiv i slovar
f = open("hw9.csv", "r", encoding="utf-8")
s = f.readlines()
f.close()
for oneline in s:
    wordinfo=oneline
    #ubiraem \n v konce strok
    if wordinfo[-1:]=="\n":
        wordinfo=wordinfo[:-1]
    wordinfo=wordinfo.split(",")
    words.append(wordinfo[0])
    hints.update({wordinfo[0]: wordinfo[1:]})

#randomno vybiraem slovo iz massiva, kotoroe zagadaet programma
theword=choice(words)
#schetchik
count=0
#telo programmy. cykl povtoryaetsya, poka polzovatel ne otgadayet zagadannoe slovo
while True:
    #kolichestvo popytok
    if count != 0:
        print("Число совершенных попыток: "+str(count))
    #podskazki budut idti po ocheredi, a kogda zakonchatsya, nachnut povtoryatsya
    print("Подсказка: "+hints[theword][count%3])
    count += 1
    i = input("Ваша догадка: ")
    if i == theword:
        break
    else:
        print("Неверно.")
#kak tolko polzovatel otgadyvaet slovo, vyvoditsya soobscheniye, chto on ugadal i chislo popytok
print("Верно.")
print("Число совершенных попыток: "+str(count))
