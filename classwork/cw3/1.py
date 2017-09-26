s=input()
x=""
a='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in s:
    if i != ' ':
        for j in range(len(a)):
            if i == a[j]:
                x+=a[(j+2)%33]
    else: x+=' '
print(x)
