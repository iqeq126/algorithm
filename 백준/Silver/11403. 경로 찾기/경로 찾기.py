N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
def floyd_warshall():
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[j][i] != 0 and graph[i][k] != 0:
                    graph[j][k] = 1
floyd_warshall()
[ print(*graph[i]) for i in range(N)]