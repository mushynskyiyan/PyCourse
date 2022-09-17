import string
rng_first = input("Введите две буквы через дефис: ")
rng_second = string.ascii_letters
i = rng_second.index(rng_first[0])
j = rng_second.index(rng_first[2])
print(rng_second[i:j+1])
