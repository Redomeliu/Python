from math import sqrt
def prime(x):
    is_prime=True
    for i in range(int(sqrt(x+1)),1,-1):
        if x%i==0:
            is_prime=False
    if x==1:
        is_prime = False
    return is_prime
            
n = int(input())
m=[]
for i in range(n):
    m.append(int(input()))
for i in range(n):
    if prime(m[i]):
        print('Yes')
    else:
        print('No')
