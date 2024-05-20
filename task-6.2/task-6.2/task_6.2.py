def books(b1, b2):
    b_lst1 = b1.split()
    b_lst2 = b2.split()
    x = set(b_lst1).intersection(set(b_lst2))
    return len(x)
s1 = input(" ")
s2 = input(" ")
c = books(s1, s2)
print(f"Ответ: {c}")

