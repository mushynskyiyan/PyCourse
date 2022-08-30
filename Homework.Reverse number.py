x = int(input('Введи пятизначное число не содержащее цифру 0 '))
n_one = x // 10000
n_two = x // 1000 % 10
n_three = x // 100 % 10
n_four = x // 10 % 10
n_five = x // 1 % 10
print(n_five * 10000 + n_four * 1000 + n_three * 100 + n_two * 10 + n_one)