lst1 = [0, 1, 2, 3, 4, 5, 7]
a = len(lst1)
b = 0
if lst1:
    for i in range(a):
        if i % 2 == 0:
            b += lst1[i]
    print(b * lst1[a - 1])
else:
    print(0)
