import sys, heapq
input = sys.stdin.readline
# 초기화
N = int(input())
h = []
for i in range(N):
    M, S, T = map(int, input().split())
    h.append((S, T))
h.sort()
classroom = []
heapq.heappush(classroom, h[0][1])
for i in range(1, N):
    if h[i][0] < classroom[0]:
        heapq.heappush(classroom, h[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, h[i][1])
print(len(classroom))