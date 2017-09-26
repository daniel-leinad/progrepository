s = input()
x=""
x+=s[:len(s)//2]
a=s[len(s)//2:]
x+=a[::-1]
print(x)
