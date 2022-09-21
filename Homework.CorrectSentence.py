def correct_sentence(str1):
    str1 = str1.strip(".")
    s = f"{str1[0].upper()}{str1[1:]}."
    return s


s1 = input("Print your sentence: ")
print(correct_sentence(s1))
