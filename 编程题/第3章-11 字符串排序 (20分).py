word =input()

for i in word:
    if i ==' 'or i=='\t' or i=='\n':
        word=word.replace(i,' ')
list1 =list(word.split())
word = sorted(list1)
print("After sorted:")
for i in word:
    print(i)
