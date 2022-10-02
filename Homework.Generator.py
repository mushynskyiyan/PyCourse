def powwe(x):
    return x ** 2


def some_gen(begin, end, func):
    for i in range(end):
        yield begin
        begin = func(begin)


print(list(some_gen(2, 4, powwe)))
