x = int(input('Input number from 0000 to 9999 '))
num_one = x // 1000
num_two = x // 100 % 10
num_three = x // 10 % 10
num_four = x // 1 % 10
print(num_one)
print(num_two)
print(num_three)
print(num_four)