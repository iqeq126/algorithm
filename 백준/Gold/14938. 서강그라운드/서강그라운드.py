import sys, heapq
input = sys.stdin.readline
n, m, r = map(int, input().split())
lst = list(map(int, input().split()))
item = [0 for _ in range(n+1)]
for i in range(1, n+1):
    item[i] = lst[i-1]
res = 0
graph = [[] for _ in range(n+1)]
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])
def dijkstra(t):
    distance = [99999999999 for _ in range(n + 1)]
    q = []
    result = 0
    heapq.heappush(q, [0, t])
    distance[t] = 0
    while q:
        nowCost, nowLoc = heapq.heappop(q)
        if distance[nowLoc] < nowCost:
            continue
        for i in graph[nowLoc]:
            cost = nowCost + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    for i in range(1, n+1):
        if distance[i] <= m:
            result += item[i]
    return result

for i in range(1, n+1):
    res = max(res, dijkstra(i))
print(res)