import sys
input = sys.stdin.readline
N, K = map(int, input().split())
wallet = []
for i in range(N):
    t = int(input())
    wallet.append(t)
wallet.sort()
DP = [0] + [ 10001 for num in range(K)  ]
for coin in wallet:
    for i in range(coin, K+1):
        DP[i] = min(DP[i], DP[i - coin] + 1)
print(-1) if DP[K] == 10001 else print(DP[K])