import sys, math, heapq
input = sys.stdin.readline
N = int(input())
q = []
gcdQ = []
for _ in range(N):
    num = int(input())
    heapq.heappush(q, num)
h1 = heapq.heappop(q)
while q:
    h2 = heapq.heappop(q)
    heapq.heappush(gcdQ, (h2-h1))

gcd = heapq.heappop(gcdQ)
while gcdQ:
    gcd = math.gcd(gcd, heapq.heappop(gcdQ))

res = set()
for i in range(2, int(gcd**0.5) + 1):
    if gcd % i == 0:
        res.add(i)
        res.add(gcd // i)
res.add(gcd)
print(*sorted(list(res)))