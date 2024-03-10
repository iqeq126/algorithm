import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    From, to, weight = map(int, input().split())
    graph[From].append([to, weight])
    graph[to].append([From, weight])
s, e = map(int, input().split())


def dijkstra(start, end):
    if start == end: return 0
    q = []
    distance = [INF for _ in range(N + 1)]
    heapq.heappush(q, [start, 0])
    distance[start] = 0
    while q:
        x, y = heapq.heappop(q)
        if distance[x] < y:
            continue
        for cur_x, cur_cost in graph[x]:
            cost = distance[x] + cur_cost
            if cost < distance[cur_x]:
                distance[cur_x] = cost
                heapq.heappush(q, (cur_x, cost))
    return distance[end]


res = dijkstra(1, s) + dijkstra(s, e) + dijkstra(e, N)
res2 = dijkstra(1, e) + dijkstra(e, s) + dijkstra(s, N)
if res >= INF and res2 >= INF:
    print(-1)
else:
    print(min(res, res2))
