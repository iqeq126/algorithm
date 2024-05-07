import sys, itertools, math
input, print = sys.stdin.readline, sys.stdout.write
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
primeList = [x for x in itertools.islice(prime_gen(), 10000)]
for i in range(n):
    p = int(input())
    if is_prime(p):
        print(f"{p}: prime\n")
    else:
        print(f"{p}:")
        while p > 1:
            for t in primeList:
                if p % t == 0:
                    p //= t
                    print(f" {t}")
                    break
        print(f"\n")