x = float(input())
if x<0:
    print("Invalid Value!")
elif x>50:
    print(f'cost = {50*0.53+(x-50)*0.58:.2f}')
else :
    print(f'cost = {x*0.53:.2f}')