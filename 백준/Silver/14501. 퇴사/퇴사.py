n = int(input())
t_lst, p_lst = [0] * n, [0] * n
dp = [0] * (n+1)
for i in range(n):
    t, p = map(int, input().split())
    t_lst[i], p_lst[i] = t, p

for i in range(n):
    for j in range(i+t_lst[i], n+1):
        if dp[j] < dp[i] + p_lst[i]:
            dp[j] = dp[i] + p_lst[i]
print(dp[-1])