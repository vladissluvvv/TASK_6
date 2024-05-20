def s(text):
    a = set()  
    b = set()
    c = set()
    for i in text:
        if i.isalpha():
            a.add(i)
        elif i.isdigit():
            b.add(i)
        else:
            c.add(i)
    return ' '.join(sorted(a)), ' '.join(sorted(b)), ' '.join(sorted(c))
x = input(" ")
a, b, c = s(x)
print(" ", a )
print(" ", b)
print(" ", c)

