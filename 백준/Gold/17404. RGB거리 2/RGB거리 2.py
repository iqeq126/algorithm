import sys
input = sys.stdin.readline
INF = 10 ** 8
ans = INF
N = int(input())
R, G, B = [0 for _ in range(N+1)], [0 for _ in range(N+1)], [0 for _ in range(N+1)]
for i in range(1, N+1):
    R[i], G[i], B[i] = map(int, input().split())
_list = [R[1], G[1], B[1]]

for i in range(3):
    DP = [[INF for _ in range(3)] for _ in range(N + 1)]
    for j in range(3):
        if j == i:
            DP[1][j] = _list[j]
        else:
            DP[i][j] = INF
    for j in range(2, N+1):
        DP[j][0] = min(DP[j - 1][1], DP[j - 1][2]) + R[j]
        DP[j][1] = min(DP[j - 1][0], DP[j - 1][2]) + G[j]
        DP[j][2] = min(DP[j - 1][0], DP[j - 1][1]) + B[j]

    for j in range(3):
        if j == i:
            continue
        ans = min(ans, DP[N][j])
print(ans)