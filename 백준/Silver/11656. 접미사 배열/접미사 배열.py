import heapq
s = list(input())
lst = []
for _ in range(len(s)):
    heapq.heappush(lst, s[_:])
for _ in range(len(s)):
    print(*heapq.heappop(lst), sep="")