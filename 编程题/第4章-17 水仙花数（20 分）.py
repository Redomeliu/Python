n = int(input())
a=10**(n-1)
sum = 0 
for i in range(a,a*10):
    t = i
    sum = 0
    for j in range(n):
        x = t % 10
        sum += x**n
        t = int(t/10)
    if(sum == i):
        print(i)
