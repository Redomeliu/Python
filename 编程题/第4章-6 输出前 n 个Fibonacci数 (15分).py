def Fibonacci(i):
    lis = [1,1]
    n = 1
    while(i>n):
        lis.append(lis[n]+lis[n-1])
        n +=1
    return lis[i]    
x = int(input())
count = 0
for i in range(x):
    count +=1
    print(f'{Fibonacci(i):>11d}',end="")
    if count == 5 or i==x-1:
        print('\n')
        count=0


if x < 1:
    print('Invalid.')
