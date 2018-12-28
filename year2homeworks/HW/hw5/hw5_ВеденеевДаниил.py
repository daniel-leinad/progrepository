from flask import Flask, render_template, request
import sqlite3
import os


app = Flask(__name__)


@app.route("/")
def index():
    if len(request.args) == 0:
        # если поиск не происходит,
        # объявляем все необходимые переменные как None
        search = False
        res = None
        num = None
        reses = None
        page = None
        pn = None
        pnall = None
    else:
        search = True
        # делаем поиск в зависимости о типа поиска
        if request.args["searchtype"] == "phrase":
            res = searchphrase(request.args["text"])
        elif request.args["searchtype"] == "word":
            res = searchword(request.args["text"])
        # pn - номер страницы, начиная от 0, pnall - общее количество страниц
        pn = int(request.args["pagen"])
        pnall = (len(res)//5)+1
        if pn > 0:
            # убираем результаты первых страниц,
            # на каждой странице - 5 результатов
            res = res[5*pn:]
        # определяем переменые нужные
        # для выведения результатов и листания страниц
        num = len(res)
        reses = min(num, 5)
        url = "/?text="+request.args["text"] + \
              "&searchtype="+request.args["searchtype"]+"&pagen="
        page = [url+str(pn-1), url+str(pn+1)]
    return render_template('index.html', res=res, search=search,
                           num=num, reses=reses, page=page, pn=pn, pnall=pnall)


# для поиска фразы
def searchphrase(x):
    # массив результатов поиска
    ret = []
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    for row in c.execute("SELECT * FROM news"):
        if x in row[2]:
            # выбираем начало и конец отрывка текста, который будет выводиться
            xstart = row[2].find(x)
            begin = max(0, xstart-150)
            end = min(len(row[2]), xstart+150)
            # ссылка - название -
            # участок до искомого - искомое - участок после искомого
            ret.append([row[0], row[1], row[2][begin:xstart],
                       row[2][xstart:xstart+len(x)],
                       row[2][xstart+len(x):end]])
    conn.close()
    return ret


# для поиска слова любой формы
def searchword(xx):
    # массив результатов поиска
    ret = []
    # с помощью mystemа определяем начальную форму слова
    f = open("input.txt", "w", encoding="utf-8")
    f.write(xx)
    f.close()
    # os.system(r"cd C:/mystem/")
    os.system(r"mystem.exe -l input.txt output.txt")
    f = open("output.txt", "r", encoding="utf-8")
    xx = f.read()
    f.close()
    # майстем не всегда определяет единственную лемму, поэтому хx - массив
    xx = xx[1:-1].split("|")
    print(xx)
    # поиск, аналогичный searchphrase()
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    for row in c.execute("SELECT * FROM news"):
        # прописываем все варианты,
        # тк майстем не всегда определяет единственную лемму
        for x in xx:
            if "{"+x+"=" in row[3]:
                # выбираем начало и конец отрывка текста,
                # который будет выводиться
                xstart = row[3].find("{"+x+"=")
                begin = max(0, xstart-150)
                end = min(len(row[3]), xstart+150)
                # ссылка - название -
                # участок до искомого - искомое - участок после искомого
                ret.append([row[0], row[1], row[3][begin:xstart],
                           row[3][xstart:xstart+len(x)+2],
                           row[3][xstart+len(x)+2:end]])
            if "{"+x+"|" in row[3]:
                # выбираем начало и конец отрывка текста,
                # который будет выводиться
                xstart = row[3].find("{"+x+"|")
                begin = max(0, xstart-150)
                end = min(len(row[3]), xstart+150)
                # ссылка - название -
                # участок до искомого - искомое - участок после искомого
                ret.append([row[0], row[1], row[3][begin:xstart],
                           row[3][xstart:xstart+len(x)+2],
                           row[3][xstart+len(x)+2:end]])
            if "|"+x+"|" in row[3]:
                # выбираем начало и конец отрывка текста,
                # который будет выводиться
                xstart = row[3].find("|"+x+"|")
                begin = max(0, xstart-150)
                end = min(len(row[3]), xstart+150)
                # ссылка - название -
                # участок до искомого - искомое - участок после искомого
                ret.append([row[0], row[1], row[3][begin:xstart],
                           row[3][xstart:xstart+len(x)+2],
                           row[3][xstart+len(x)+2:end]])
            if "|"+x+"=" in row[3]:
                # выбираем начало и конец отрывка текста,
                # который будет выводиться
                xstart = row[3].find("|"+x+"=")
                begin = max(0, xstart-150)
                end = min(len(row[3]), xstart+150)
                # ссылка - название -
                # участок до искомого - искомое - участок после искомого
                ret.append([row[0], row[1], row[3][begin:xstart],
                           row[3][xstart:xstart+len(x)+2],
                           row[3][xstart+len(x)+2:end]])
    conn.close()
    return ret


if __name__ == "__main__":
    app.run(debug=False)
