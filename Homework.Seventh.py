lst2 = [1, 0, 3, 0, 0, 0, 5]
lst3 = []
lst4 = []
a = len(lst2)
for i in range(a):
    if lst2[i] != 0:
        lst3.append(lst2[i])
    elif lst2[i] == 0:
        lst4.append(lst2[i])
print(lst3 + lst4)