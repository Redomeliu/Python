s = input()
count =0
yuan ="AEIOU"
for i in s:
    if 'A'<=i<='Z' and i not in yuan:
        count +=1
print(count)
