n = int(input())
x = 1
s = 0
for i in range(0,n):
    s += 1/x
    x += 2
print(f'sum = {s:.6f}')