s = input()
l = list(s)
l = list(set(l))
l = sorted(l)
s = "".join(l)

print(s)
