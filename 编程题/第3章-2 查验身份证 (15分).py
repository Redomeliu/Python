def judge(b, m, c):
    sum = 0
    x = 0
    for i in b[0:17]:
        if '0' <= i <= '9':
            sum =sum+int(i) * c[x]
            x +=1
        else:
            return False
    z = sum % 11
    if m[z] == b[-1]:
        return True
    else:
        return False
    
a = int(input())
count = 0
c = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
m = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
for x in range(a):
        b= input()
        if not judge(b, m, c):
            print(b)
        else:
            count +=1
if count == a:
    print("All passed")
