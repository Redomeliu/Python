n = int(input())
if n>0 and n<=1000:
    x = [i for i in range(1,n+1)]
    j = 0
    k = 0
    while(len(x)>2):
        y = []
        for j in x:
            k += 1
            if k!=3:
                y.append(j)
            else:
                k = 0
        x = y
    if(len(x)==2):
        x = x[1]
    else:
        x = x[0]
    print(x)
else:
    print(0)
    exit(0)
