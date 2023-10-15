import sys, heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
V, E = map(int, input().split())
INF = sys.maxsize
graph = defaultdict(list)
heap = []
connected = [False] *(V+1)
for i in range(E):
    A, B, C = map(int, input().split())
    if i == 0:
        heap.append([0,A])
    graph[A].append([C, B])
    graph[B].append([C, A])
MST, cnt = 0, 0
while heap:
    if cnt == V:
        break
    w, v = heapq.heappop(heap)
    if not connected[v]:
        connected[v] = True
        MST += w
        cnt += 1
        for i in graph[v]:
            heapq.heappush(heap, i)
print(MST)
