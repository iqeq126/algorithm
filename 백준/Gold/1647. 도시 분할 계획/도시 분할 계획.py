from collections import defaultdict
from heapq import heappop, heappush
import sys
graph = defaultdict(list)
input = sys.stdin.readline
N, M = map(int, input().split())
mst = [False] * (N+1)
for i in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append([e, cost])
    graph[e].append([s, cost])

def prim(N=N):
    res, max_cost = 0, 0
    q = [[0, 1]]
    while q:
        cost, node = heappop(q)
        if mst[node]: continue
        mst[node] = True
        if cost > max_cost:
            max_cost = cost
        res += cost
        N -= 1
        if N == 0: return res - max_cost
        for next_node, next_cost in graph[node]:
            if not mst[next_node]:
                heappush(q, [next_cost, next_node])
print(prim())