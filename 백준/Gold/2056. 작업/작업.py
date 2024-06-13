from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
depth = [0] * (n+1)
dp = [0] * (n+1)
sequence = [[] for _ in range(n+1)]
task = [0]
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    task.append(lst[0])
    l = len(lst)
    if l >= 2:
        for j in range(2, l):
            sequence[lst[j]].append(i)
            depth[i] += 1
def bfs():
    q = deque()
    for i in range(1, n+1):
        if not depth[i]:
            q.append(i)
            dp[i] = task[i]
    while q:
        c = q.popleft()
        for i in sequence[c]:
            depth[i] -= 1
            if dp[c] + task[i] > dp[i]:
                dp[i] = dp[c] + task[i]
            if not depth[i]:
                q.append(i)
    return max(dp)
print(bfs())