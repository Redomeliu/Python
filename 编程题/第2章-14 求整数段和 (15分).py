a,b = map(int,input().split())
sum = 0
i = 0
for index in range(a,b+1):
    if i==5:
        print()
        i=0
    sum += index
    print(f'{index:>5d}', end='')
    i +=1
print()
print('Sum = %d' % sum)
