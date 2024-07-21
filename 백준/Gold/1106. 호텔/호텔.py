import sys
input = sys.stdin.readline
c, n = map(int, input().split())
lst = list( list(map(int, input().split()) )for _ in range(n))
dp = [0] + [ 10 ** 7 for _ in range(c+100)]

for cost, people in lst:
    for i in range(people, c+100):
        dp[i] = min(dp[i - people] + cost, dp[i])
print(min(dp[c:]))