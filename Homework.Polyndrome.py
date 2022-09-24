import string


def is_palindrome(a):
    a = a.lower()
    a1 = a
    for i in range(len(a)):
        if a[i] in string.punctuation or a[i] in " ":
            a1 = a1.replace(a[i], "")
    b = a1[::-1]
    if a1 == b:
        c = True
    else:
        c = False
    return c


word = str(input("Enter word or phrase: "))
print(is_palindrome(word))