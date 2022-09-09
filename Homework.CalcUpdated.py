ask = 'yes'
while ask == 'yes' or ask == 'y':
    a = float(input('Please enter number '))
    a_oper = input('Choose operation + , - , * , / ')
    b = float(input('Please enter number '))
    if a_oper == '+':
        print(a + b)
    elif a_oper == '-':
        print(a - b)
    elif a_oper == '*':
        print(a * b)
    elif a_oper == '/':
        if b != 0:
            print(a / b)
        else:
            print('Divide by 0 can destroy universe \nPlease do not attempt to do it again')
    else:
        print('Mission impossible \nYou should choose valid operation')
    ask = input('If you want to continue please type "yes" ')
    ask = ask.lower()
print("""Thank you for using my best calculator for this moment 
\nSee you next time""")