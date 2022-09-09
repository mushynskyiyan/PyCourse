'''
Пользователь вводит строку. Ваша задача - проверить, может ли эта строка, быть именем переменной.

Переменная не может начинаться с цифры, состоять только из цифр, не может содержать заглавные буквы и знаки пунктуации,
кроме нижнего подчеркивания "_" . Также, она не может быть ни одним из зарегистрированных слов.
При этом имя переменной, может состоять только из одного нижнего подчеркивания "_" .
Зарегистрированные слова можно взять из keyword.kwlist
В итоге проверки, на печать выводится True, если такое имя переменной допустимо, и False - в противном случае.
Примеры имен переменных и результат (=> на печать выводить не нужно :))

_ => True
x => True
get_value => True
Get_value => False
get_Value => False
getValue => False
3m => False
'''

import keyword
import string

user_var = input('Please enter variable name ')
a = len(user_var)
okvar = True
if user_var.count('_') > 1:
    okvar = False
if user_var.isdigit():
    okvar = False
if user_var[0] in string.digits:
    okvar = False
if user_var in keyword.kwlist:
    okvar = False

for i in range(a):
    if user_var[i] in string.ascii_uppercase:
        okvar = False
    elif user_var[i] in string.punctuation and '_' not in user_var[i]:
        okvar = False
print(okvar)