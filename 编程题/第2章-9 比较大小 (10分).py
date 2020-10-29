a,b,c = map(int,input().split())
if a>c: a,c =  c,a
if a>b: a,b = b,a
if b>c: b,c = c,b
print('%d->%d->%d' % (a,b,c))
