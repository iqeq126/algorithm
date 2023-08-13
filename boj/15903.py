import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
for i in range(m):
    a, b = heapq.heappop(card), heapq.heappop(card)
    heapq.heappush(card, a+b)
    heapq.heappush(card, a+b)
print(sum(card))
