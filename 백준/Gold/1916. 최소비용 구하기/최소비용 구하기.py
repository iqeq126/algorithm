import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [ INF for _ in range(N+1) ]
for i in range(M):
    From, to, weight = map(int, input().split())
    graph[From].append([to, weight])

s, e = map(int, input().split())
def dijkstra():
    q = []
    heapq.heappush(q, [0, s])
    distance[s] = 0
    while q:
        y, x = heapq.heappop(q)
        if distance[x] < y:
            continue
        for i in graph[x]:
            cost = distance[x] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra()
print(distance[e])