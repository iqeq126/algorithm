import sys
from collections import defaultdict
input= sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    From, to, weight = map(int, input().split())
    if graph[From][to] > weight:
        graph[From][to] = weight

def floyd_warshall():
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if graph[j][i] != INF and graph[i][k] != INF:
                    graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
floyd_warshall()
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j or graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
