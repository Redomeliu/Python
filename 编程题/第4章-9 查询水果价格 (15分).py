print("[1] apple\n[2] pear\n[3] orange\n[4] grape\n[0] exit")
a = list(map(int,input().split(" ")))
for i in range(0,5):
    if a[i]==0:
        break
    elif a[i]==1:
        print("price = 3.00")
    elif a[i]==2:
        print("price = 2.50")
    elif a[i]==3:
        print("price = 4.10")
    elif a[i]==4:
        print("price = 10.20")
    else:
         print("price = 0.00")
