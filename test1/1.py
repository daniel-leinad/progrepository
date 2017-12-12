f = open("Ozhegov.txt", "r", encoding="utf8")
s = f.read()
s=s.split("\n")
f.close()
for i in s:
    a=i.split("|")
    if len(a[0])>=20:
        print(i)
