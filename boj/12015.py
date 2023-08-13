import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = []
D = [0] * (N+1)
B.append(A[0])
ans = 0
now = 0
for i in range(1, N):
    if A[i] > B[ans]:
        B.append(A[i])
        D[i] = ans + 1
        ans += 1
        # print(B[:ans+1])
    else:
        #print(bisect_left(B, A[i]), A[i])
        D[i] = bisect_left(B, A[i])
        B[D[i]] = A[i]
#    else:
#        D[i] = b_search(0, ans, B, A[i])
#        B[now] = B[b_search(0, ans, B, A[i])]
#        A[D[i]] = min(B[i], B[now])
#        now = D[i]
print(ans+1)