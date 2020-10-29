a, n = map(int, input().split())
sum = 0
b = 0
for i in range(1, n+1):
    b = b+a
    sum += b
    b *=10
print(f's = {sum}')