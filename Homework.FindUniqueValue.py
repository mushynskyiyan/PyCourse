def find_unique_value(lst1):
    uniq_value = 0
    for i in range(len(lst1)):
        if lst1.count(lst1[i]) == 1:
            uniq_value = lst1[i]
    return uniq_value


list_of_values = [5, 5, 5, 0.5]
print(find_unique_value(list_of_values))
