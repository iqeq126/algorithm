import itertools, math
n = int(input())

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i = i + 2
    return True

def prime_gen():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n

primeList = [x for x in itertools.islice(prime_gen(), 10001)]
print(primeList[n-1])