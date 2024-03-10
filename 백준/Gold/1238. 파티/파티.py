import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize
N, M, x = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    From, to, weight = map(int, input().split())
    graph[From].append([to, weight])

def dijkstra(start, end):
    if start == end: return 0
    q = []
    distance = [INF for _ in range(N + 1)]
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        y, x = heapq.heappop(q)
        if distance[x] < y:
            continue
        for cur_x, cur_cost in graph[x]:
            cost = distance[x] + cur_cost
            if cost < distance[cur_x]:
                distance[cur_x] = cost
                heapq.heappush(q, (cost, cur_x))
    return distance[end]


answer = -1
for i in range(1, N+1):
    res = dijkstra(i, x) + dijkstra(x, i)
    if answer <= res:
        answer = res
print(answer)
