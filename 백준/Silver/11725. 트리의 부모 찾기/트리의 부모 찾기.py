import sys
from collections import deque, defaultdict
input = sys.stdin.readline
dic = defaultdict(list)
N = int(input())
dic[1] = [1]
for _ in range(N-1):
    x, y = map(int, input().split())
    dic[x].append(y)
    dic[y].append(x)
q = deque([1])
parent = defaultdict(int)
while q:
    cur = q.popleft()
    for i in dic[cur]:
        if parent[i] == 0 and i != 1:
            parent[i] = cur
            q.append(i)
for _ in range(2, N+1):
    print(parent[_])