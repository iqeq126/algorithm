import sys
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline
T = int(input())
def dikstra(s):
    q = []
    heappush(q, [0, s])
    dist = [ int(1e9) for _ in range(n+1)]
    dist[s] =  0

    while q:
        weight, now = heappop(q)
        for next, next_weight in graph[now]:
            res_weight = weight + next_weight
            if res_weight < dist[next]:
                dist[next] = res_weight
                heappush(q, [res_weight, next])
    return dist


for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        a, b, d = map(int, input().split())
        heappush(graph[a], (b, d))
        heappush(graph[b], (a, d))

    lst = [0] * t
    for _ in range(t):
        lst[_] = int(input())

    S, G, H = dikstra(s), dikstra(g), dikstra(h)
    res = []
    for i in lst:
        if S[g] + G[h] + H[i] == S[i] or S[h] + H[g] + G[i] ==S[i]:
            res.append(i)
    print(*sorted(res))