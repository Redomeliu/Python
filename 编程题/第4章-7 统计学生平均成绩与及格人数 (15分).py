a = int(input())
if a==0:
    print(f'average = 0.0\ncount = 0')
    exit(0)
b = list(map(int,input().split(" ")))
sm = sum(b)
average = sm/a
pas = [x for x in b if x>=60]
count = len(pas)
print(f'average = {average:.1f}\ncount = {count}')
