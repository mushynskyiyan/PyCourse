'''Для списка целых чисел нужно найти сумму элементов с четными индексами [0-й, 2-й, 4-й итд],
затем перемножить эту сумму на последний элемент исходного массива.
Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 [ноль].
[0, 1, 2, 3, 4, 5] => (0 + 2 + 4) * 5 = 30
[1, 3, 5] => 30
[6] => 36
[] => 0'''

lst1 = [6]
a = len(lst1)
b = 0
if lst1:
    for i in range(a):
        if i % 2 == 0:
            b += lst1[i]
    print(b * lst1.pop())
else:
    print(0)
