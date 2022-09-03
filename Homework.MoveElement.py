lst1 = [1, 2, 'Hello', 'Buddy']
lst2 = lst1.copy()
if len(lst1) > 0:
    a = lst1.pop()
    lst1.insert(0, a)
    print(lst2, ' => ', lst1)
else:
    print(lst2, ' => ', lst1)
