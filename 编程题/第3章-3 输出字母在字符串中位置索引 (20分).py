char = input()
m, n = input().split()
char =char[::-1]
for i in range(0,len(char)):
    if(n==char[i]):
        print(f'{len(char)-i-1:d} {n:s}')
for i in range(0,len(char)):
    if(m==char[i]):
        print(f'{len(char)-i-1:d} {m:s}')
    
