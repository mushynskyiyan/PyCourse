n = input("Введите число: ")
if int(n) > 0:
    while int(n) > 10:
        k = 1
        for i in range(len(str(n))):
            k = k * int(str(n)[i])
        n = k
    print(n)
else:
    print("You entered invalid number")