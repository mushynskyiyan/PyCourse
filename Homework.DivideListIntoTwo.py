lst1 = [1, 2, 3, 4, 5, 6]
lst2 = list()
if len(lst1) % 2 == 0:
    mida = len(lst1) // 2
    lst2.extend([lst1[:mida], lst1[mida:len(lst1)]])
    print(lst1, " => ", lst2)
else:
    midb = len(lst1) // 2
    lst2.extend([lst1[:midb + 1], lst1[midb + 1:len(lst1)]])
    print(lst1, " => ", lst2)

'''
lst3 = [1, 2, 3, 4, 5]
lst4 = list()
if len(lst3) % 2 == 0:
    midc = len(lst3) // 2
    lst4.extend([lst1[:midc], lst1[midc:len(lst3)]])
    print(lst3, " => ", lst4)
else:
    midd = len(lst3) // 2
    lst4.extend([lst3[:midd + 1], lst3[midd + 1:len(lst3)]])
    print(lst3, " => ", lst4)

'''
'''
lst5 = [1]
lst6 = list()
if len(lst5) % 2 == 0:
    mide = len(lst5) // 2
    lst6.extend([lst5[:mide], lst5[mide:len(lst5)]])
    print(lst5, " => ", lst6)
else:
    midf = len(lst5) // 2
    lst6.extend([lst5[:midf + 1], lst5[midf + 1:len(lst5)]])
    print(lst5, " => ", lst6)

'''
'''
lst7 = []
lst8 = list()
if len(lst7) % 2 == 0:
    midg = len(lst7) // 2
    lst8.extend([lst7[:midg], lst7[midg:len(lst7)]])
    print(lst7, " => ", lst8)
else:
    midh = len(lst7) // 2
    lst8.extend([lst7[:midh + 1], lst7[midh + 1:len(lst7)]])
    print(lst7, " => ", lst8)
'''
