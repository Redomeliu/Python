def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def funcos(eps, x):
    i = 0
    s = 0
    k = 1
    while x ** i / factorial(i) > eps or x ** i / factorial(i) == eps:
        i = i + 2
    for j in range(0, i, 2):
            s = s + k * x ** j / factorial(j)
            k = -k
    return s

eps = float(input())
x = float(input())
value = funcos(eps, x)

print("cos({0}) = {1:.4f}".format(x,value))