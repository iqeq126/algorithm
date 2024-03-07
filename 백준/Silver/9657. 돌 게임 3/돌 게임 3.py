DP = [0, 1, 0, 1, 1] + [0] * 1000
N = int(input())
for i in range(5, 1003):
    if DP[i-1] + DP[i-3] + DP[i-4] < 3:
        DP[i] = 1
    else:
        DP[i] = 0
print("SK") if DP[N] else print("CY")