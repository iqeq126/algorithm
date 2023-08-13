import sys
input = sys.stdin.readline
N, D = map(int, input().split())
graph = []
distance = [0 for i in range(D+1)]
for i in range(N):
    s, e, l = map(int, input().split())
    graph.append([s, e, l])
for i in range(1, D+1):
    distance[i] = distance[i-1] + 1
    for j in range(N):
        if graph[j][1] == i:
            distance[i] = min(distance[i], min(distance[i-1]+1, graph[j][2] + distance[graph[j][0]]))
graph.sort()
print(distance[D])