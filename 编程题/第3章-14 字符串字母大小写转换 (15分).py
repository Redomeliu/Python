x = input()
y = ""
for i in x:
    if i.islower():
        i = i.upper()
    else:
        i = i.lower()
    y += i
y = y[0:-1]

print(y)
