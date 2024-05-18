import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
res = 0
B = [-A[0]]
answer = [A[0]] * (n+1)

for i in range(1, n):
    A[i] -= i
    heappush(B, -A[i])
    answer[i+1] = -B[0]+i
    if A[i] < -B[0]:
        res += B[0] - A[i]
        heappop(B)
        heappush(B, -A[i])

for i in range(n-1, -1, -1):
    answer[i] = min(answer[i], answer[i+1]-1)

for i in range(1,n+1):
    print(answer[i])

