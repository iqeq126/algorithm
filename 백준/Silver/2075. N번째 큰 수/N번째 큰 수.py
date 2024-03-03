import sys, heapq
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    buf = list(map(int, input().split()))
    if not lst:
        for b in buf:
            heapq.heappush(lst, b)
    else:
        for b in buf:
            if lst[0] < b:
                heapq.heappush(lst, b)
                heapq.heappop(lst)
print(heapq.heappop(lst))