N = int(input())
def floyd_warshall():
    graph = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[j][i] != 0 and graph[i][k] != 0:
                    graph[j][k] = 1
    return graph
print('\n'.join(' '.join(map(str, row)) for row in floyd_warshall()))