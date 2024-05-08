from collections import defaultdict
N = int(input())
MOD = 1000000007
DP = defaultdict(int)
DP[0], DP[1], DP[2] = 0, 1, 1
def get_fibo(n, MOD):
    if n > 2 and DP[n] == 0:
        mid = n // 2
        if n % 2:
            m1, m2 = get_fibo(mid+1, MOD), get_fibo(mid, MOD)
            DP[n] = (m1 ** 2 + m2 ** 2) % MOD
        else:
            m1, m2 = get_fibo(mid, MOD), get_fibo(mid-1, MOD)
            DP[n] = ((2 * m2 + m1) * m1) % MOD
    return DP[n]
print(get_fibo(N, MOD))