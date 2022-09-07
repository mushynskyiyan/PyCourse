lst1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
a = len(lst1)
b = 0
for i in range(a):
    if lst1[i] != 0:
        lst1[b], lst1[i] = lst1[i], lst1[b]
        b +=1
print(lst1)