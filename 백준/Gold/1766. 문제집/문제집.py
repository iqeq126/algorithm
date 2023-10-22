import sys
from heapq import *
input = sys.stdin.readline
N, M = map(int, input().split())
degree = [0 for _ in range(N+1)]
student = [[] for _ in range(N+1)]
for _ in range(M):
    fi, se = map(int, input().split())
    student[fi].append(se)
    degree[se] += 1
result = []
q = []
for i in range(1, N+1):
    if degree[i] == 0:
        heappush(q, i)
while q:
    now = heappop(q)
    result.append(now)
    for node in student[now]:
        degree[node] -= 1
        if degree[node] == 0:
            heappush(q, node)
print(*result)