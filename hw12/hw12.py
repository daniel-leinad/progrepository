#variant 5
import os
import re

flist = os.listdir()
count = 0
for i in flist:
    if os.path.isdir(i):
        if re.match(r".*\b.+\b.*\b.+\b.*", i):
            count += 1

print("Названия всех папок и файлов:")
for i in flist:
    print(i)
print("Найдено папок, название которых состоит из более чем одного слова:")
print(count)
