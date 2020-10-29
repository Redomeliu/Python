s = input()
judge = True
for i in range(len(s)):
    if s[i] != s[-i-1]:
        judge = False
if judge:
    print ("Yes")
else:
    print("No")
