
"""“”“prime(p)，返回True表示p是素数，返回False表示p不是素数
PrimeSum(m,n)，函数返回素数和
"""
def prime(p):
    from math import sqrt
    is_prime = True
    for index in range(int(sqrt(p)), 1, -1):
        if p % index == 0:
            is_prime = False
            break
    if p != 1 and is_prime:
        return True
        print(p)
    else:
        return False
def PrimeSum(m, n):
    s = 0
    for index in range(m, n+1):
        if prime(index):
            s += index
    return s


m, n = input().split()
m = int(m)
n = int(n)
print(PrimeSum(m, n))