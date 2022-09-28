def difference(*args):
    if args:
        min_element = args[0]
        max_element = args[0]
    else:
        return 0
    for i in args:
        if i < min_element:
            min_element = i
    for j in args:
        if j > max_element:
            max_element = j
    diff = max_element - min_element
    return diff


a = difference(10.2, -2.2, 0, 1.1, 0.5)
print(round(a, 1))
