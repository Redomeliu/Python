lower,upper = map(int,input().split())
if lower > upper:
    print('Invalid.')
else:
    print('fahr celsius')

    for F in range(lower,upper+1,2):
        C = 5*(F-32)/9
        print("{:d}{:>6.1f}".format(F,C))
