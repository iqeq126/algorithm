import sys
input, print = sys.stdin.readline, sys.stdout.write
n = int(input())
dp = [0] * 10001
dp[0] = dp[1] = dp[2] = 1
for i in range(3, 10001):
    dp[i] = dp[i-1] + dp[i-2]
for i in range(n):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {dp[a] % b}\n")