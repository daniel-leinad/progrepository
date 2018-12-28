import sqlite3


f = open("mystem/metadata.csv", "r", encoding="utf-8")
lines = f.readlines()
f.close()


conn = sqlite3.connect("news.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS news(link TEXT PRIMARY KEY, name TEXT, plain TEXT, mystempl TEXT)")


for line in lines[1:]:
    thelink = line.split("\t")[10]
    thepath = line.split("\t")[0][2:]
    thename = line.split("\t")[2]
    #если файла по какой-то причине нет, пропускаем его
    try:
        fh = open("mystem/"+thepath, "r")
    except:
        print(thepath)
        continue
    try:
        fh = open("mystem/mystem-"+thepath, "r", encoding="utf-8")
    except:
        print("mystem-"+thepath)
        continue

    
    fpl = open("mystem/"+thepath, "r")
    theplain = fpl.readlines()
    fpl.close()
    theplain = theplain[5:]
    theplain = "".join(theplain)

    
    fmspl = open("mystem/mystem-"+thepath, "r", encoding="utf-8")
    themystempl = fmspl.read()
    fmspl.close()

    
    c.execute("INSERT INTO news VALUES (?,?,?,?)", (thelink, thename, theplain, themystempl))
for row in c.execute("select * from news"):
    print(row[0])
conn.commit()
conn.close()
