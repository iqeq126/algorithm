import sys
input = sys.stdin.readline
# 첫째 줄에 두 수 n과 m이 빈 칸을 사이에 두고 순서대로 주어진다.
#  n은 집하장의 개수,  m은 집하장간 경로의 개수
INF = sys.maxsize
N, M = map(int, input().split())
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
nodes = [['-' for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    S, E, weight = map(int, input().split())
    graph[S][E] = graph[E][S] = weight
    nodes[S][E] = E
    nodes[E][S] = S

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if j == k:
                continue

            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
                nodes[j][k] = nodes[j][i]



for i in range(1, N+1):
    for j in range(1, N+1):
        if j == N:
            print(nodes[i][j])
        else:
            print(nodes[i][j], end=" ")

