import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
degree = [0 for _ in range(N+1)]
student = [[] for _ in range(N+1)]
for _ in range(M):
    fi, se = map(int, input().split())
    student[fi].append(se)
    degree[se] += 1
result = []
q = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    result.append(now)
    for node in student[now]:
        degree[node] -= 1
        if degree[node] == 0:
            q.append(node)
print(*result)