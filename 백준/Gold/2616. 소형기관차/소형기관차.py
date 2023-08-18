import sys
input = sys.stdin.readline
N = int(input())
_list = list(map(int, input().split()))
M = int(input())
t = -1
ans = 0
sum_list = [0 for _ in range(N+1)]
DP = [[0 for _ in range(N+1)] for _ in range(4)]
for i in range(1, N+1):
    sum_list[i] = sum_list[i-1] + _list[i-1]

for i in range(1, 4):
    for j in range(N+1):
        DP[i][j] = 0
        if j >= M:
            DP[i][j] = max(DP[i][j-1], DP[i-1][j-M] + (sum_list[j] - sum_list[j-M]))
        ans = max(DP[i][j], ans)
print(ans)