import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [0] + list(map(int, input().split()))
C = [0] * M
res = 0
for i in range(1, N+1):
    lst[i] += lst[i-1]
    lst[i] %= M
    if lst[i] == 0: res += 1
    C[lst[i]%M] += 1
for i in range(M):
    if C[i]:
        # 시그마 연산
        res += C[i] * (C[i]-1) // 2
print(res)