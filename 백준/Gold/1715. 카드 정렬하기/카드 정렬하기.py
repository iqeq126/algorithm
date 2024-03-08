import sys, heapq
input = sys.stdin.readline
N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))
res = 0
while len(cards) > 1:
    card1, card2 = heapq.heappop(cards), heapq.heappop(cards)
    res += (card1 + card2)
    heapq.heappush(cards, card1 + card2)
print(res)