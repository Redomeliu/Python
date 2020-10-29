x=input()
s=input()
n = -1
for index in range(0,len(s)):
    if s[index]==x:
        n = index
if(n != -1):
    print("index = %d" % n)
else:
    print("Not Found")
