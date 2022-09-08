import random

lst1 = []
a = random.randint(3, 10)
for i in range(a):
    lst1.append(random.randint(1, 20))

lst2 = [lst1[0], lst1[2], lst1[-2]]
print(lst1, ' => ', lst2)