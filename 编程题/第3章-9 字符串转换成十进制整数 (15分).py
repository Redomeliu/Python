st = input()
s = ' '
for i in st:
    if i=='#':
        break
    s +=i
for i in s:
    if not('0'<=i<='9' or 'a'<=i<='f' or 'A'<=i<='F' or i=='-'):
        s=s.replace(i,' ')
    if 'a' <= i <= 'f':
        i= i.upper()
s=s.replace(' ','')
a = ''
if s[0]=='-':
    a = '-'
s=s.replace('-','')
s=s.replace(' ','')
if s != '':
	print('{0}{1}'.format(a, int(s, 16)))
else:
	print(0)
