def is_prime(k):
    for i in range(2, k):
        if k % i == 0:
            break
    else:
        return True


def prime_generator(x):
    for i in range(1, x):
        if is_prime(i):
            yield i


print(list(prime_generator(20)))


