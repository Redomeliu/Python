t = input().split()
mylist = [int(t[i]) for i in range(0, len(t))]
ave = sum(mylist)/len(t)
for index in range(0,len(t)):
    if mylist[index]>ave :
        print(mylist[index] , end = " ")
