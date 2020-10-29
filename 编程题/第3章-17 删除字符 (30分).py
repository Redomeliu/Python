str = input()
s = input()
s = s.strip()
m=""
for i in str:
    if i != s.upper() and i != s.lower():
        m +=i
m =m.strip()
print("result: %s" % m)
