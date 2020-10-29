def factorial(x):
    sum =1
    for i in range(1,x+1):
        sum *=i
    return sum

n = int(input())
sum = 1
for i in range(1,n+1):
    sum += 1/factorial(i)
print(f'{sum:.8f}')
