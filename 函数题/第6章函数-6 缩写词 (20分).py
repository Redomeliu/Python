def acronym(phrase):
    a = phrase.title()
    b = a.split()
    m = ''
    for i in b:
        c = i.strip()
        d = c[0]
        m += d
    return m
phrase=input()
print(acronym(phrase))