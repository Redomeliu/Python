lis = list(map(int,input().split()))
lis , times,one= lis[1:],0,0
for i in lis:
    num = lis.count(i)
    if num>times:
            one = i
            times = num

print("%d %d" % (one,times))
