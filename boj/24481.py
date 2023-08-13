from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
global index
index = 1
def dfs(graph, dfs_list, depth_list, v, visited, depth):
    visited[v] = True
    depth += 1
    global index
    dfs_list[v] = index
    depth_list[v] = depth
    for i in graph[v]:
        if not visited[i]:
            index += 1
            dfs(graph, dfs_list, depth_list, i, visited, depth)

N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
dfs_list = [0] * (N+1)
depth_list = [-1] * (N+1)
for i in range(M):
    edge_1, edge_2 = map(int, sys.stdin.readline().split())
    graph[edge_1].append(edge_2)
    graph[edge_2].append(edge_1)
for i in graph:
    graph[i].sort()
visited = [False] * (N+1)
dfs(graph, dfs_list, depth_list, V, visited, -1)
for i in range(1, N+1):
    print(depth_list[i])