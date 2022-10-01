import string


def first_word(str1):
    str2 = str1
    for i in range(len(str1)):
        if str1[i] in string.punctuation and "'" not in str1[i]:
            str2 = str1.replace(str1[i], " ")
    lst1 = str2.split()
    return lst1[0]


import_string = input("Enter words: ")
print("First word is: ", first_word(import_string))

