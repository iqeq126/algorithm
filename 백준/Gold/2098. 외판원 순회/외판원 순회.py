from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = defaultdict(int)
def TSP(cur, visited):
    if visited == (1 << N) -1:
        if W[cur][0]: return W[cur][0]
        else: return float('inf')
    if (cur, visited) in dp:
        return dp[(cur, visited)]

    res = float('inf')
    for i in range(1, N):
        if not W[cur][i] or visited & (1 << i):
            continue
        if res >= TSP(i, visited | (1 << i)) + W[cur][i]:
            res = TSP(i, visited | (1 << i)) + W[cur][i]
    dp[(cur, visited)] = res
    return dp[cur, visited]
print(TSP(0, 1))