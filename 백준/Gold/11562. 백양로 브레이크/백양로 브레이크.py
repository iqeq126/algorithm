import sys
input = sys.stdin.readline
INF = sys.maxsize
# Y대학교 건물의 수 n과 길의 수 m이 주어진다. (n ≤ 250, m ≤ n * (n - 1) / 2 )
N, M = map(int, input().split())
#  u v b (1 ≤ u ≤ n, 1 ≤ v ≤ n, u != v, b = 0 또는 1) 의 형태로 길에 대한 정보가 주어진다.
# b가 0일 경우 u에서 v로 가는 일방통행 길인 것이고, b가 1일 경우 u와 v를 잇는 양방향 길이다.
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
for _ in range(M):
    U, V, B = map(int, input().split())
    graph[U][V] = 0
    graph[V][U] = 0
    if B == 0:
        graph[V][U] = 1

# 플로이드-워셜
def floyd_warshall():
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]
floyd_warshall()

# 다음 k줄에 걸쳐 s e (1 ≤ s ≤ n, 1 ≤ e ≤ n)의 형태로 학생들의 질문들이 주어진다.
# 이는 질문한 학생이 건물 s에서 건물 e로 가고 싶다는 의미이다.
K = int(input())
for _ in range(K):
    S, E = map(int, input().split())
    # 각 질문에 대해, 최소 몇 개의 일방통행인 길을 양방향 통행으로 바꿔야 출발지에서 도착지로 갈 수 있는지를 출력한다.
    # 모든 길을 양방향으로 바꾸더라도 서로 도달 불가능한 건물은 없다.
    print(graph[S][E])