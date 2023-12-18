import sys
input= sys.stdin.readline
N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    lst = list(map(int, input().split()))
    for j in range(1, N+1):
        graph[i][j] = lst[j-1]


def floyd_warshall():
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
floyd_warshall()
for i in range(M):
    Y, X, W = map(int, input().split())
    if graph[Y][X] <= W:
        print("Enjoy other party")
    else:
        print("Stay here")
