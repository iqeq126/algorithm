import itertools, math, sys
input, print = sys.stdin.readline, sys.stdout.write
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

primeList = [x for x in itertools.islice(prime_gen(), 1300)]
t = int(input())
for i in range(t):
    a = int(input())
    print(f"Input value: {a}\n")
    if a in primeList:
        print("Would you believe it; it is a prime!\n\n")
    else:
        j = 0
        while primeList[j] < a:
            j += 1
        res = min(abs(a - primeList[j]), abs(a - primeList[j-1]))
        print(f"Missed it by that much ({res})!\n\n")