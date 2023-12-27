import sys, heapq
input = sys.stdin.readline
def getLength(d1x, d1y, d2x, d2y):
    return ( (d2x-d1x) ** 2 + (d2y - d1y) ** 2) ** 0.5

# 발전소의 수(N), 남아있는 전선 수(W)
N, W = map(int, input().split())
# 제한 길이(M)
M = float(input())
lst = [[0,0]]
graph = [[] for _ in range(N+1)]
for i in range(N):
    # 1~N번 발전소 각각의 x, y좌표 입력
    x, y = map(int, input().split())
    lst.append([x, y])
for i in range(1, N+1):
    for j in range(i+1, N+1):
        L = getLength(lst[i][0], lst[i][1], lst[j][0], lst[j][1])
        if L <= M:
            graph[i].append([j, L])
            graph[j].append([i, L])

for j in range(W):
    # 각각의 발전소 연결
    n1, n2 = map(int, input().split())
    graph[n1].append([n2, 0])
    graph[n2].append([n1, 0])
# 1번 발전소와 N번 발전소를 잇는데 필요한 추가 전선 길이의 최솟값을 1,000배 하여 출력(버림 연산)
def dijkstra():
    lengths = [sys.maxsize for _ in range(N+1)]
    lengths[1] = 0
    q = []
    heapq.heappush(q, [1,0])
    while q:
        curLoc, curLen = heapq.heappop(q)
        if lengths[curLoc] < curLen: continue
        for nextLoc, nextLen in graph[curLoc]:
            if lengths[nextLoc] > curLen + nextLen:
                lengths[nextLoc] = curLen + nextLen
                heapq.heappush(q, [nextLoc, curLen + nextLen])
    print( int(lengths[N] * 1000))
dijkstra()