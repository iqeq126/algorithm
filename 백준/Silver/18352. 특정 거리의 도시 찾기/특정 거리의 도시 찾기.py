# 시간 복잡도
# 공간 복잡도
# 풀이 시간
# 참고 링크

import sys, heapq
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
tag = -1
graph = [[] for _ in range(N+1)]
distance = [ sys.maxsize for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append([B,1])
def dijkstra():
    q = []
    heapq.heappush(q, [0, X])
    distance[X] = 0
    while q:
        y, x = heapq.heappop(q)
        for i in graph[x]:
            cost = distance[x] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra()
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        tag = i
if tag == -1:
    print(tag)