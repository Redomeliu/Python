from math import sqrt
def prime(x):
    is_prime = True
    for i in range(int(sqrt(x))+1,1,-1):
        
        if(x%i==0):
            is_prime = False
    return is_prime
N = int(input())
for i in range(2,int(N/2)+1):
    if prime(i) and prime(N-i):
        print(f'{N} = {i} + {N-i}')
        break
