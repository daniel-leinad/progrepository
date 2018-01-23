import random
#5 ВАРИАНТ
"""
Обозначениния рода и падежа:
род:
мужской - 0
женский - 1
средний - 2
падеж:
именительный - 0
винительный - 1
"""

###СЧИТЫВАЕМ ФАЙЛЫ
#считываем файл с существительными
f = open("nouns.txt", "r", encoding="utf-8")
nouns=f.read().split("\n")
f.close()
for i in range(len(nouns)):
    nouns[i] = nouns[i].split()
    nouns[i][2]=int(nouns[i][2])

#считываем файл с глаголами
f = open("verbs.txt", "r", encoding="utf-8")
verbs=f.read().split("\n")
f.close()

#считываем файл с прилагательными
f = open("adjectives.txt", "r", encoding="utf-8")
adjectives=f.read().split("\n")
f.close()

#считываем файл с наречиями
f = open("adverbs.txt", "r", encoding="utf-8")
adverbs=f.read().split("\n")
f.close()

#считываем файл с союзами
f = open("soyuzy.txt", "r", encoding="utf-8")
soyuzy=f.read().split("\n")
f.close()

"""
Система такая:
предложение (sent())
состоит из двух частей (clause()),
соединенных союзом (souyuz()) (сложносочинительным или сложноподчинительным),
каждая часть состоит из подлежащего и его зависимых (podlezh())
и сказуемого и его зависимых (skaz()).
"""
def noun(case):
    #функция возвращает случайное существительное, стоящее в нужном падеже, и род этого существительного (для согласования)
    res = random.choice(nouns)
    return [res[case],res[2]]

def verb(gender):
    #функция возвращает случайный глагол, стоящий в нужном роде
    if gender == 0:
        return random.choice(verbs)
    elif gender == 1:
        return random.choice(verbs)+"а"
    elif gender == 2:
        return random.choice(verbs)+"о"

def adjective(gender):
    #функция возвращает случайное прилагательное, стоящее в нужном роде
    if gender == 0:
        return random.choice(adjectives)
    elif gender == 1:
        return random.choice(adjectives)[:-2]+"ая"
    elif gender == 2:
        return random.choice(adjectives)[:-2]+"ое"

def adverb():
    #функция возвращает случайное наречие
    return random.choice(adverbs)

def soyuz():
    #функция возвращает случайный союз
    return random.choice(soyuzy)

def podlezh():
    #функция возврает подлежащее и его зависимые
    res = noun(0)
    v = random.choice([0,1,2])
    #выбирается один из случаев:
    #0 - только подлежащее
    #1 - подлежащее и зависящее от него определение
    #2 - подлежащее, зависящее от него определение и зависящее от определения наречие
    if v == 0:
        return [res[0],res[1]]
    elif v == 1:
        return [adjective(res[1])+" "+res[0],res[1]]
    elif v == 2:
        return [adverb()+" "+adjective(res[1])+" "+res[0],res[1]]

def skaz(gender):
    #функция возвращает сказуемое и его зависимые
    res=""
    #от сказуемого может зависеть наречие
    if random.choice([True, False]):
        res+=adverb()+" "
    res+=verb(gender)
    #от сказуемого может зависеть прямое дополнение
    if random.choice([True, False]):
        res+=" "+noun(1)[0]
    return res

def clause():
    #функция возвращает часть предложения
    res = podlezh()
    return res[0]+" "+skaz(res[1])

def sent():
    #функция возвращает предложение с заглавной буквы
    res = clause()+", "+soyuz()+" "+clause()+"."
    return res[0].upper()+res[1:]


#Основной код - выводит 5 предложений.
for i in range(random.choice([5,6,7,8,9,10])):
    print(sent())
