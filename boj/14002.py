import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = []
C = []
D = [0] * (N+1)

B.append(A[0])
ans = 0
for i in range(1, N):
    if A[i] > B[ans]:
        B.append(A[i])
        D[i] = ans + 1
        ans += 1
    else:
        D[i] = bisect_left(B, A[i])
        B[D[i]] = A[i]
now = ans
if now == 0:
    print(1)
    print(*B[:ans+1])
else:
    for i in range(N, -1, -1):
        if D[i] == now:
            C.append(A[i])
            now -= 1
            if now == -1:
                break
    C = C[::-1]
    print(ans+1)
    # print(*D[:N])
    print(*C[:ans+1])