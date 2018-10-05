import urllib.request
import json


token = "0bf126491d24ccf797445e574a9843d41e21069e"


def userdata(us, whichdata):
    # Данная функция возвращает объект питона для нужного пользователя с сайта
    theurl = "https://api.github.com/users/%s/%s?access_token=%s" % \
            (us, whichdata, token)
    response = urllib.request.urlopen(theurl)
    text = response.read().decode('utf-8')
    return json.loads(text)


def repositories(us):
    print("Имя репозитория - его описание")
    data = userdata(us, "repos")
    for rep in data:
        print(str(rep["name"]) + " - " + str(rep["description"]))
        # выводим данные для каждого репозитория
    return None


def languages(us):
    print("Язык - количество репозиториев в котором он используется")
    languages = {}  # словарь в формате язык:число использований
    data = userdata(us, "repos")
    for rep in data:
        if str(rep["language"]) in languages:
            languages[str(rep["language"])] += 1
            # если язык уже был в словаре - увеличиваем значение на 1
        else:
            languages[str(rep["language"])] = 1
            # если еще не было - создаем новый ключ
    for lang in languages:
        print(lang + " - " + str(languages[lang]))  # выводим словарь
    return None


def biggestrep(lofu):
    print("Пользовател(ь/и) с наибольшем количеством репозиториев:")
    bestus = []  # список из пользователей
    # с наибольшим количеством репозиториев (на случай если их несколько)
    bestnum = 0  # максимальное число репозиториев у пользователя
    for us in lofu:
        data = userdata(us, "repos")
        if len(data) == bestnum:
            bestus.append(us)
            # если число реп. совпадает с максимальным - добавляем в список
        elif len(data) > bestnum:
            bestnum = len(data)
            bestus = [us]  # если число реп. больше максимального -
            # делаем его единственным в списке, меняем максимальное число
    print(", ".join(bestus))  # выводим всех польлзователей через запятую
    return None


def poplang(lofu):
    print("Самые популярные языки:")
    langs = {}  # словарь в формате язык:число использований
    for us in lofu:
        data = userdata(us, "repos")
        for rep in data:
            if str(rep["language"]) in langs:
                langs[str(rep["language"])] += 1
                # если язык был в словаре - увеличиваем значение на единицу
            else:
                langs[str(rep["language"])] = 1
                # если не было - добавляем в словарь
    k = 0  # максимальное число использования языка
    poplangs = []  # список с самыми популярными языками
    for lang in langs:
        if lang == "None":
            continue
        if langs[lang] == k:
            poplangs.append(lang)
            # если число использований совпадает
            # с максимальным - добавляем в список
        elif langs[lang] > k:
            poplangs = [lang]
            k = langs[lang]
            # если число использований больше максимального -
            # делаем язык единственным в списке, меняем максимальное число
    print(", ".join(poplangs))  # выводим языки через запятую
    return None


def mostfollowers(lofu):
    print("Пользовател(ь/и) с наибольшем количеством фолловеров:")
    bestus = []  # список с пользователями с наибольшим колвом фолловеров
    bestnum = 0  # максимальное количество фолловеров
    for us in lofu:
        data = userdata(us, "followers")
        if len(data) == bestnum:
            bestus.append(us)
        elif len(data) > bestnum:
            bestnum = len(data)
            bestus = [us]  # меняем максимальное число
    print(", ".join(bestus))  # выводим пользователей через запятую
    return None


def main(lofu):
    us = input("Напишите порядковый номер нужного вам пользователя: ")
    while True:
        # этот цикл нужн для того, чтобы пользователь мог ввести только число
        if us.isnumeric():
            us = int(us)
            break
        else:
            us = ("Пожалуйста, введите только цифру")
    repositories(lofu[us-1])
    print()
    languages(lofu[us-1])
    print()
    biggestrep(lofu)
    print()
    poplang(lofu)
    print()
    mostfollowers(lofu)
    return None


usnames = []
print("Введите имена пользователей, последнюю строку оставьте пустой")
i = 1
while True:
    s = input(str(i) + ". ")
    if s == "":
        break
    else:
        usnames.append(s)
    i += 1
main(usnames)
