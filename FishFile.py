import string


def count_words(fle):
    fle2 = fle
    for i in range(len(fle)):
        if fle[i] in string.punctuation and "'" not in fle[i]:
            fle2 = fle.replace(fle[i], " ")
    lst1 = fle2.split()
    cnt = len(lst1)
    return cnt


def count_expressions(fle):
    cn_ex = fle.count('. ')
    return cn_ex


def count_strings(fil):
    cstr = fil.count('\n')
    return cstr


fl = open('/Users/jan/Desktop/file.txt', encoding="utf-8")
flr = fl.read()
new_file = open('/Users/jan/Desktop/newfile.txt', "x", encoding="utf-8")
new_file.close()
new_file = open('/Users/jan/Desktop/newfile.txt', "a", encoding="utf-8")
new_file.write(f'Words: {count_words(flr)} \n'
               f'Expressions: {count_expressions(flr)} \n'
               f'Strings: {count_strings(flr)}')
fl.close()
new_file.close()





