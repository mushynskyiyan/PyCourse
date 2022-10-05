def generate_cube_numbers(x):
    for i in range(2, x):
        i = i ** 3
        if i < x:
            yield i
        else:
            return


value = input("Enter number: ")
print(list(generate_cube_numbers(int(value))))


