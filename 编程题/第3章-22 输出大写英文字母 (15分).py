s = input()
st = ""
for i in s:
    if i.isupper() and i not in st:
        st += i
if len(st)!=0 :
    print(st)
else:
    print("Not Found")
