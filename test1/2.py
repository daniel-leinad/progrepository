f = open("Ozhegov.txt", "r", encoding="utf8")
s = f.read()
s=s.split("\n")
f.close()
count = 0
for string in s:
    a = string.split("|")
    if len(a)>=3 and a[2] != "":
        count+=1
print(count)

