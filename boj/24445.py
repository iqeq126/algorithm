from collections import defaultdict, deque
import sys
def bfs(graph, bfs_list, s, Q, visited):
    visited[s] = True
    cnt = 1
    bfs_list[s] = cnt
    while Q:
        node = Q.popleft()
        for v in graph[node]:
            if visited[v] is False:
                cnt += 1
                visited[v] = True
                Q.append(v)
                bfs_list[v] = cnt
    return bfs_list
N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
bfs_list = [0] * (N+1)
for i in range(M):
    edge_1, edge_2 = map(int, sys.stdin.readline().split())
    graph[edge_1].append(edge_2)
    graph[edge_2].append(edge_1)
for i in graph:
    graph[i].sort(reverse=True)
Q = deque([V])
visited = [False] * (N+1)
num = 1
bfs(graph, bfs_list, V, Q, visited)
print(*bfs_list[1:], sep="\n")