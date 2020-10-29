string = input()
inpstr = ""
text = [chr(letter)for letter in range(65, 91)]
retext = text[::-1]
for i in string:
    if i in text:
        i = retext[text.index(i)]
    inpstr +=i
print(inpstr)
