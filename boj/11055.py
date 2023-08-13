import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = []
D = [0] * (N*1)
ans = 0
B.append(A[0])
for i in range(N):
    if A[i] > B[ans]:
        B.append(A[i])
        D[i] = ans+1
        ans +=1
    else:
        D[i] = bisect_left(B, A[i])
        B[D[i]] = A[i]

max = 0
buf = 0
print(*D[:])
for i in range(N-1, -1, -1):
    now = D[i]
    buf = 0
    for j in range(i, -1, -1):
        if D[j] == now:
            buf += A[j]
            now -= 1
            if now < 0:
                break
    if buf < max:
        max = buf
print(max)