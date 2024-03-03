import sys, heapq
input = sys.stdin.readline
N, K = int(input()), int(input())
lst = sorted(list(map(int, input().split())))
if K > N:
    print(0)
else:
    dist = []
    for i in range(1, N):
        heapq.heappush(dist, lst[i-1]-lst[i])
    for i in range(K-1):
        heapq.heappop(dist)
    print(-sum(dist))