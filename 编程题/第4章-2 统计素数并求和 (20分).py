def prime(p):
    from math import sqrt
    is_prime = True
    for index in range(int(sqrt(p)), 1, -1):
        if p % index == 0:
            is_prime = False
            break
    if p != 1 and is_prime:
        return True
    else:
        return False
def PrimeSum(m, n):
    s = 0
    count=0
    for index in range(m, n+1):
        if prime(index):
            s += index
            count +=1
    return count,s

m, n = input().split()
m = int(m)
n = int(n)
(a,b)=PrimeSum(m, n)
print(a,b)
