def rim(str):
    lst = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    i = 0
    while i < len(str):
        a = str[i]
        x = str[i + 1] if i + 1 < len(str) else None

        if x and lst[a] < lst[x]:
            n += lst[x] - lst[a]
            i += 2
        else:
            n += lst[a]
            i += 1
    return n
while True:
    rim_num = input(" ")
    if rim_num == ' ':
        break
    d_num = rim(rim_num)
    print(f"{rim_num} = {d_num}")
