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