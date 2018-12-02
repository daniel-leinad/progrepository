import json
from flask import Flask
from flask import url_for, render_template, request, redirect


# создаем csv файл
f = open("reses.csv", "w", encoding="utf-8")
f.write("город;имя;пол;род\n")
f.close()


# словарь для страниццы статистики
reses = {"msc": {},
         "spb": {},
         "sochi": {},
         "other": {},
         "m": {},
         "f": {},
         "o": {}
         }
for i in reses:
    reses[i]["m"] = 0
    reses[i]["n"] = 0
    reses[i]["f"] = 0
    reses[i]["o"] = 0


# переменная со всеми данными
jsoon = []


# переменные для поиска
exchange = {"msc": "Москвы",
            "spb": "Санкт-Петербурга",
            "sochi": "Сочи",
            "other": "других городов",
            "m": "мужского",
            "f": "женского",
            "o": "разного"
            }
coffee = {"m": "мой кофе",
          "n": "мое кофе",
          "f": "моя кофе",
          "o": "@#%& кофе"
          }


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("ankete.html")


@app.route("/collect")
def collect():
    if ";" in request.args["name"] or len(request.args["name"]) == 0:
        # чтобы это не мешалось случайно в csv таблице
        # и чтобы не было пустых имен
        return render_template("error.html")
    else:
        try:
            f = open("reses.csv", "a", encoding="utf-8")
            f.write(request.args["city"]+";"+request.args["name"] +
                    ";"+request.args["sex"]+";"+request.args["coffee"]+"\n")
            f.close()
        except:
            return render_template("error.html")
        else:
            jsoon.append(request.args)
            reses[request.args["city"]][request.args["coffee"]] += 1
            reses[request.args["sex"]][request.args["coffee"]] += 1
            return render_template("thanks.html")


@app.route("/stats")
def stats():
    return render_template("stats.html", res=reses)


@app.route("/json")
def jayson():
    return json.dumps(jsoon)


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/results")
def results():
    ssex = request.args["sex"]
    scity = request.args["city"]
    sres = []
    for i in jsoon:
        if i["sex"] == ssex and i["city"] == scity:
            sres.append({"name": i["name"], "coffee": coffee[i["coffee"]]})
    return render_template("results.html",
                           sex=exchange[ssex], city=exchange[scity], res=sres)


if __name__ == "__main__":
    app.run(debug=True)
