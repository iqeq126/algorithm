import sys
input = sys.stdin.readline
N, M = map(int, input().split())
res = [0]
for i in range(1, N+1): res.append(int(input()) + res[i-1])
DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
visited = [[False for _ in range(M+1)] for _ in range(N+1)]
def range_split(r, s):
    if s == 0: return 0
    if r <= 0: return -3276800
    if visited[r][s]: return DP[r][s]
    visited[r][s] = True
    DP[r][s] = range_split(r-1,s)
    for i in range(r, 0, -1):
        DP[r][s] = max(DP[r][s], range_split(i-2, s-1) + res[r]-res[i-1])
    return DP[r][s]
print(range_split(N,M))