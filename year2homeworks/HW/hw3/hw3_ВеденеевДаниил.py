import urllib.request
from bs4 import BeautifulSoup
import os

def isreal(theurl):
    req = urllib.request.Request(theurl, headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('windows-1251')
    return html.find('<div class="mndata"></div>') == -1

def lastnum(tpc):
    # эта функция определяет номер последней статьи в выбранном топике
    theurl = 'http://www.surskieprostori.ru/news-'+tpc+'.html'
    req = urllib.request.Request(theurl, headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('windows-1251')
    x = html.find('<div class="onemidnew">')
    y = html.find('<a href="/news-'+tpc+'-',x)
    yy = html.find('.html">',y)
    return int(html[y+len('<a href="/news-'+tpc+'-'):yy])

def between(t, b):
    x = t.find(b[0])
    y = t.find(b[1], x)
    return t[x+len(b[0]):y]

def putfileto(directory, filetype, content):
    if not os.path.exists(directory):
        os.makedirs(directory)
    i = 1
    while True:
        if not os.path.exists(directory+'статья'+str(i)+'.'+filetype):
            break
        i += 1
    name = 'статья'+str(i)+'.'+filetype
    f = open(directory+name, 'w')
    f.write(content)
    f.close()

def plain(datas):
    cntnt = '@au '+datas['au']+'\n'
    cntnt += '@ti '+datas['ti']+'\n'
    cntnt += '@da '+datas['da']+'\n'
    cntnt += '@topic '+datas['topic']+'\n'
    cntnt += '@url '+datas['url']+'\n'
    cntnt += datas['text']
    direc = './plain/'+datas['da'].split('.')[2]+'/'+datas['da'].split('.')[1]+'/'
    putfileto(direc, 'txt', cntnt)

def mystemxml(datas):
    pass

def mystemtxt(datas):
    pass

def rootcsv(datas):
    f = open('metadata.csv', 'a+')
    f.write('\n')
    metadata = []
    path = './plain/'+datas['da'].split('.')[2]+'/'+datas['da'].split('.')[1]+'/'
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
    f = open('metadata.csv', 'w')
    f.write('path\tauthor\theader\tcreated\tsphere\ttopic\tstyle\taudience_age\taudience_level\taudience_size\tsource\tpublication\tpubl_year\tmedium\tcountry\tregion\tlanguage')
    f.close()

def pagedatas(theurl):
    req = urllib.request.Request(theurl, headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('windows-1251')
    thetext = between(html,['</h2></div>', '<p></p>'])
    soup = BeautifulSoup(thetext, 'html.parser')
    datas = {}
    datas['text'] = soup.get_text()
    datas['au'] = 'None'
    # Автор не везде указан, а там, где указан - не отделить однозначно от текста
    datas['ti'] = between(html, ['<div class="mnname"><h2>', '</h2></div>'])
    datas['topic'] = between(html, ['<h1>', '</h1>'])
    datas['da'] = between(html, ['<div class="mndata">', '</div>'])
    datas['url'] = theurl
    return datas


topics = ['1','31','37','20','11','10','8','7','5','3']
# номера соответствуют интересующим нас отделам
createcsv()
for tpic in topics:
    num = lastnum(tpic)
    xxx = 0
    while True:
        url = 'http://www.surskieprostori.ru/news-'+tpic+'-'+str(num)+'.html'
        if isreal(url):
            xxx += 1
            newsdatas = pagedatas(url)
            rootcsv(newsdatas)
            plain(newsdatas)
            mystemxml(newsdatas)
            mystemtxt(newsdatas)
        if xxx >=50:
            break
        num -= 1
