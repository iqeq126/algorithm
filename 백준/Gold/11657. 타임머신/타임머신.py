import sys
INF = sys.maxsize
V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))
def bellmanford(start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    for i in range(V):
        for s, e, w in edges:
            if dist[s] != INF and dist[e] > dist[s] + w:
                if i == V - 1:
                    print(-1)
                    return
                dist[e] = dist[s] + w
    for i in range(2, V+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
bellmanford(1)