import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = [A[0]]
D = [0] * (N*1)
res = 0
for i in range(N):
    D[i] = A[i]
    for j in range(i):
        if A[i] > A[j] and D[i] < D[j] + A[i]:
            D[i] = D[j] + A[i]
    if res < D[i]:
        res = D[i]
print(res)