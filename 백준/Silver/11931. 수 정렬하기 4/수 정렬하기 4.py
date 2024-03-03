import sys, heapq
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    heapq.heappush(lst, -int(input()))
for _ in range(N):
    print(-heapq.heappop(lst))