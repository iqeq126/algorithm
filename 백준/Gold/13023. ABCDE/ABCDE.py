from collections import defaultdict
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = defaultdict(list)
visited = set()
res = False
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(index, depth):
    global res
    visited.add(index)
    if depth == 4:
        res = True
        return
    
    for i in graph[index]:
        if i not in visited:
            visited.add(i)
            dfs(i, depth+1)
            visited.remove(i)
for i in range(n):
    dfs(i, 0)
    visited.remove(i)
    if res:
        print(1)
        sys.exit()
print(0)