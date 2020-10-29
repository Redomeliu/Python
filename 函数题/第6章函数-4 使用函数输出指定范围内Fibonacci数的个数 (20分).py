def fib(n):
    if(n==0)or(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
def PrintFN(m,n):
    s = []
    for i in range(n):
        if fib(i) > n:
            break
        if m<=fib(i)<=n:
            s.append(fib(i))
    return s

m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
b=fib(i)
print("fib({0}) = {1}".format(i,b))
fiblist=PrintFN(m,n)
print(len(fiblist))