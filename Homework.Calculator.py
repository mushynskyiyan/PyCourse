a = float(input('Введите число '))
a_oper = input('Выберите действие + , - , * , / ')
b = float(input('Введите число '))
if a_oper == '+':
    print(a + b)
elif a_oper == '-':
    print(a-b)
elif a_oper == '*':
    print(a*b)
elif a_oper == '/':
    if b != 0:
        print(a/b)
    else:
        print('Деление на 0 невозможно')
else:
    print('Действие невозможно')