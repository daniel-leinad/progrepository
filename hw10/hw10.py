#variant 5
import re
filename=input("Введите имя файла: ")
#otkryvaem nuzhniy fayl i schityvaem text ves' v lowercase
f = open(filename, "r", encoding="utf-8")
text = f.read().lower()
f.close()
#ispolzuem regularnie virazheniya
allres = re.findall(r"\b(съе(м|шь|ст|дим|дите|дят|шьте|л[аои]?|в|вш(ий|его|ему|им|ем|ее|ая|ей|ую|ею|ие|их|ими)|денн(ый|ого|ому|ым|ом|ое|ая|ой|ую|ою|ые|ых|ыми)|ден[аоы]?)(с[яь])?)\b", text)
#vivodim na pechat'
for i in allres:
    print(i[0])
