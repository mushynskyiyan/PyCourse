def is_even(a):
    a = str(a)
    eve = "02468"
    if a[-1] in eve:
        return True
    else:
        return False



с = 2494563894038**2
d = 1056897**2
e = 24945638940387**3
print(is_even(с))
print(is_even(d))
print(is_even(e))

b = int(input("Enter number: "))
print(is_even(b))
