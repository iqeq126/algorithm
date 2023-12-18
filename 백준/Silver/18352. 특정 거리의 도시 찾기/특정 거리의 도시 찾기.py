# 시간 복잡도 :
# 공간 복잡도 : O(N+1)
# 풀이 시간 : 1h
# 참고 링크 : 이전 나의 최단경로 문제 풀이

import sys, heapq
input = sys.stdin.readline
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
N, M, K, X = map(int, input().split())
# 최단 거리가 K인 도시가 하나도 없을 때 출력하기 위한 tag 정보
tag = -1

# 그래프 및 거리 정보 저장
graph = [[] for _ in range(N+1)]
distance = [ sys.maxsize for _ in range(N+1)]

# 거리가 1인 A -> B 단방향 그래프 정의
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append([B,1])
# 다익스트라 진행
def dijkstra():
    # 큐에 X에 대한 정보 입력. 자기 자신과의 거리 0, 자기 자신의 좌표 X
    q = []
    heapq.heappush(q, X)
    distance[X] = 0
    # 진행
    while q:
        now = heapq.heappop(q)
        for next, dist in graph[now]:
            cost = distance[now] + dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, next)
dijkstra()
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        tag = i
if tag == -1:
    print(tag)