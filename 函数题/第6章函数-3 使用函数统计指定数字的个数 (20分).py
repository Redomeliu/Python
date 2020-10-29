def CountDigit(number,digit ):
    s = 0
    num = str(number)
    for i in num:
        if i == str(digit):
            s += 1
    return s
number, digit=input().split()
number = int(number)
digit = int(digit)
count = CountDigit(number, digit)
print("Number of digit 2 in "+str(number)+":", count)