import urllib.request
from bs4 import BeautifulSoup
import os
# по не совсем ясной проблеме с кодировками
# программе не удается сделать разметку всем
# скачанным статьям, поэтому в папке plain будет
# больше файлов, чем в папках mystem
# это можно изменить, если ытр. 192-198 изменить на
"""
            try:
                newsdatas = pagedatas(url)
                newsdatas['direc'] = plain(newsdatas)
                mystem(newsdatas)
            except:
                if os.path.exists(newsdatas['direc']):
                    os.remove(newsdatas['direc'])
                xxx -= 1
            else:
                rootcsv(newsdatas)
"""
# однако менять код и заново выгружать все страницы уже поздно
# поэтому я решил оставить тот код, которым я выгружал статьи


u_a = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
        'AppleWebKit/537.36 (KHTML, like Gecko) ' \
        'Chrome/60.0.3112.113 Safari/537.36'


def isreal(theurl):
    req = urllib.request.Request(theurl, headers={'User-agent': u_a})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('windows-1251')
    return html.find('<div class="mndata"></div>') == -1


def lastnum(tpc):
    # эта функция определяет номер последней статьи в выбранном топике
    theurl = 'http://www.surskieprostori.ru/news-' + tpc + '.html'
    u_a = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
        'AppleWebKit/537.36 (KHTML, like Gecko) ' \
        'Chrome/60.0.3112.113 Safari/537.36'
    req = urllib.request.Request(theurl, headers={'User-agent': u_a})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('windows-1251')
    x = html.find('<div class="onemidnew">')
    y = html.find('<a href="/news-' + tpc + '-', x)
    yy = html.find('.html">', y)
    return int(html[y + len('<a href="/news-' + tpc + '-'):yy])


def between(t, b):
    x = t.find(b[0])
    y = t.find(b[1], x)
    return t[x + len(b[0]):y]


def putfileto(directory, filetype, content):
    if not os.path.exists(directory):
        os.makedirs(directory)
    i = 1
    while True:
        if not os.path.exists(directory + 'статья' + str(i) + '.' + filetype):
            break
        i += 1
    name = 'статья' + str(i) + '.' + filetype
    f = open(directory + name, 'w')
    f.write(content)
    f.close()
    return directory + name


def plain(datas):
    cntnt = '@au ' + datas['au'] + '\n'
    cntnt += '@ti ' + datas['ti'] + '\n'
    cntnt += '@da ' + datas['da'] + '\n'
    cntnt += '@topic ' + datas['topic'] + '\n'
    cntnt += '@url ' + datas['url'] + '\n'
    cntnt += datas['text']
    direc = './plain/' + \
        datas['da'].split('.')[2] + '/' + \
        datas['da'].split('.')[1] + '/'
    res = putfileto(direc, 'txt', cntnt)
    return res


def mystemxml(datas):
    f = open('input.txt', 'w', encoding='utf-8')
    f.write(datas['text'])
    f.close()
    os.system(r'cd C:/mystem/')
    os.system(r'mystem.exe -l --format xml input.txt output.txt')
    f = open('output.txt', 'r')
    restext = f.read()
    f.close()
    direct = './mystem-xml/' + '/'.join(datas['direc'].split('/')[2:-1]) + '/'
    putfileto(direct, 'xml', restext)


def mystem(datas):
    f = open('input.txt', 'w', encoding='utf-8')
    f.write(datas['text'])
    f.close()
    os.system(r'cd C:/mystem/')

    os.system(r'mystem.exe -c -l -i -g -d --eng-gr input.txt output.txt')
    f = open('output.txt', 'r')
    restext = f.read()
    f.close()
    direct = './mystem-plain/' + \
        '/'.join(datas['direc'].split('/')[2:-1]) + '/'
    putfileto(direct, 'txt', restext)

    os.system(r'mystem.exe -c -l -i -g -d --eng-gr --format '
              'xml input.txt output.txt')
    f = open('output.txt', 'r')
    restext = f.read()
    f.close()
    direct = './mystem-xml/' + '/'.join(datas['direc'].split('/')[2:-1]) + '/'
    putfileto(direct, 'xml', restext)


def rootcsv(datas):
    f = open('metadata.csv', 'a+', encoding='utf-8')
    f.write('\n')
    metadata = []
    path = datas['direc']
    metadata.append(path)
    metadata.append(datas['au'])
    metadata.append(datas['ti'])
    metadata.append(datas['da'])
    metadata.append('публицистика')
    metadata.append(datas['topic'])
    metadata.append('нейтральный')
    metadata.append('н-возраст')
    metadata.append('н-уровень')
    metadata.append('районная')
    metadata.append(datas['url'])
    metadata.append('СУРСКИЕ ПРОСТОРЫ')
    metadata.append(datas['da'].split('.')[2])
    metadata.append('газета')
    metadata.append('Россия')
    metadata.append('г. Пенза')
    metadata.append('ru')
    f.write('\t'.join(metadata))
    f.close()


def createcsv():
    f = open('metadata.csv', 'w', encoding='utf-8')
    f.write(
        'path\tauthor\theader\tcreated\t'
        'sphere\ttopic\tstyle\taudience_age\t'
        'audience_level\taudience_size\tsource\t'
        'publication\tpubl_year\tmedium\tcountry\tregion\tlanguage')
    f.close()


def pagedatas(theurl):
    req = urllib.request.Request(theurl, headers={'User-agent': u_a})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('windows-1251')
    thetext = between(html, ['</h2></div>', '<p></p>'])
    soup = BeautifulSoup(thetext, 'html.parser')
    datas = {}
    datas['text'] = soup.get_text()
    # теперь заменяем все точки на точку и перенос строки
    datas['text'] = '.\n'.join(datas['text'].split('.'))
    datas['au'] = 'None'
    # Автор не везде указан, а там, где указан -
    # не отделить однозначно от текста
    datas['ti'] = between(html, ['<div class="mnname"><h2>', '</h2></div>'])
    datas['topic'] = between(html, ['<h1>', '</h1>'])
    datas['da'] = between(html, ['<div class="mndata">', '</div>'])
    datas['url'] = theurl
    return datas


topics = ['1', '31', '37', '20', '11', '10', '8', '7', '5', '3']
# номера соответствуют интересующим нас отделам
createcsv()
for tpic in topics:
    num = lastnum(tpic)
    xxx = 0
    while True:
        url = 'http://www.surskieprostori.ru/news-' + \
            tpic + '-' + str(num) + '.html'
        if isreal(url):
            xxx += 1
            print(xxx)
            # счетчик чтобы не запутаться
            try:
                newsdatas = pagedatas(url)
                newsdatas['direc'] = plain(newsdatas)
                rootcsv(newsdatas)
                mystem(newsdatas)
            except:
                xxx -= 1
        if xxx >= 50:
            # чтобы скачало 50*10 = 500, что по приблизительным
            # расчетам должно быть больше 100к слов
            break
        num -= 1
os.remove('input.txt')
os.remove('output.txt')
