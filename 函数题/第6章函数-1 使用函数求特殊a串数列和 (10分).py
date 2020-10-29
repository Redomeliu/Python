def fn(a, n):
    y = 0
    for index in range(1, n+1):
        x = a*index
        y *= 10
        y += x
    return y

a , b = input().split()
s = fn(int(a), int(b))
print(s)