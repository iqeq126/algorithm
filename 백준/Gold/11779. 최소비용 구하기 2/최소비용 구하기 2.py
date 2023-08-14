import sys, heapq
sys.setrecursionlimit(10**8)
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
    Q = [s for _ in range(N+1)]
    while q:
        y, x = heapq.heappop(q)
        if distance[x] < y:
            continue
        for i in graph[x]:
            cost = distance[x] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                Q[i[0]] = x
                heapq.heappush(q, (cost, i[0]))
    curr = e
    path = []
    while curr != s:
        path.append(curr)
        curr = Q[curr]
    if s not in path:
        path.append(s)
    print(distance[e])
    print(len(path))
    print(*path[::-1])
dijkstra()