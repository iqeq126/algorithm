import sys, math
PI = math.pi
sys.setrecursionlimit(10**5)
t = 1000000000000000000
P = dict()
n = int(input())
def pibo(N):
    if 0 <= N <= PI:
        return 1

    if N in P:
        return P[N]

    P[N] = pibo(N-1) + pibo(N-PI)
    return P[N] % t

print(pibo(n))