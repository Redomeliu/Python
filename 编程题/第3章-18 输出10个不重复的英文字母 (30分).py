s = input()
m = ""
for i in s:
    if i.isalpha() and i.lower() not in m and i.upper() not in m:
        m +=i
    if len(m) == 10:
        break
if len(m)!=10:
    print("not found")
else:
    print(m)
