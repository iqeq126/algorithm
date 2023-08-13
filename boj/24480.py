from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
global index
index = 1
def dfs(graph, dfs_list, v, visited):
    visited[v] = True
    global index
    dfs_list[v] = index
    for i in graph[v]:
        if not visited[i]:
            index += 1
            dfs(graph, dfs_list, i, visited)

N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
dfs_list = [0] * (N+1)
for i in range(M):
    edge_1, edge_2 = map(int, sys.stdin.readline().split())
    graph[edge_1].append(edge_2)
    graph[edge_2].append(edge_1)
for i in graph:
    graph[i].sort(reverse = True)
visited = [False] * (N+1)
dfs(graph, dfs_list, V, visited)
for i in range(1, N+1):
    print(dfs_list[i])