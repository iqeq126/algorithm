import sys
input = sys.stdin.readline
n, m = map(int, input().split())
schools = [''] + list(input().split())
graph = []
for i in range(m):
    u, v, d = map(int, input().split())
    graph.append((d, u, v))
graph.sort()

parent_list = [i for i in range(n+1)]
res, cnt = 0, 1

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, s, e):
    s = find(parent, s)
    e = find(parent, e)
    if s < e:
        parent[e] = s
    else:
        parent[s] = e
for d, u, v in graph:
    if schools[u] != schools[v] and find(parent_list, u) != find(parent_list, v):
        union(parent_list, u, v)
        res += d
        cnt += 1
    if cnt == n: break

print(res) if cnt == n else print(-1)

