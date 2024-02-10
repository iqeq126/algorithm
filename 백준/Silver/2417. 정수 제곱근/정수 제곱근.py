import math
N = int(input())
if int(math.isqrt(N)) ** 2 == N:
    print(int(math.isqrt(N)))
else:
    print(int(math.isqrt(N))+1)