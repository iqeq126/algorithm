import sys
input = sys.stdin.readline
T = int(input())
while T:
    N = int(input())
    C = [0] + list(map(int, input().split()))
    for i in range(1, N): C[i+1] += C[i]
    DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N-i+1):
            DP[j][i + j] = sys.maxsize
            for k in range(j, i+j):
                DP[j][i+j] = min(DP[j][i+j], DP[j][k] + DP[k+1][i+j] + C[i+j]-C[j-1])
    print(DP[1][N])
    T -= 1