import sys
INF = sys.maxsize
t = int(input())

lst = list(int(input()) for _ in range(t))

l_dp, s_dp = [''] * 101, [f'{INF}'] * 101

l_dp[0], l_dp[1] = '1', '7'
l_dp[2], l_dp[3], l_dp[4], l_dp[5], l_dp[6], l_dp[7] = '1', '7', '11', '71', '111', '711'
s_dp[2], s_dp[3], s_dp[4], s_dp[5], s_dp[6], s_dp[7], s_dp[8], s_dp[9], s_dp[10], s_dp[11] = '1', '7', '4', '2', '6', '8', '10', '18', '22', '26'

for i in range(8, 101):
    l_dp[i] = f'1{l_dp[i-2]}' if i % 2 == 0 else f'{l_dp[i-2]}1'

for i in range(8, 101):
    for j in range(2, i-1):
        s_dp[i] = f"{min(int(s_dp[i]), int(s_dp[j] + s_dp[i-j]))}"
        if j == 6:
            s_dp[i] = f"{min(int(s_dp[i]), int(s_dp[i-j] + '0'))}"
for i in lst:
    print(s_dp[i], l_dp[i])
