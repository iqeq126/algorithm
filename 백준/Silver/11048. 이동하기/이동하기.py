import sys, copy
input = sys.stdin.readline
n, m = map(int, input().split())
miro = [[0] * (m+1) for _ in range(n+1)]
dp = copy.deepcopy(miro)
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    for j in range(1, m+1):
        dp[i][j] = miro[i][j] = lst[j-1]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = miro[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
print(dp[-1][-1])