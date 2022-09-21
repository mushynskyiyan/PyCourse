import random

lst1 = []
lst2 = []
a = random.randint(5, 20)
b = random.randint(5, 15)
j = 3
k = 5
for i in range(a):
    lst1.append(j)
    j += 3
for i in range(b):
    lst2.append(k)
    k += 5
set1 = set(lst1)
set2 = set(lst2)
set3 = set1.intersection(set2)
print(set1)
print(set2)
print(set3)
