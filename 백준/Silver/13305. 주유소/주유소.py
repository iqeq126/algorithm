import sys
input = sys.stdin.readline
N = int(input())
distance = list(map(int, input().split()))
oilBank = list(map(int, input().split()))
sum, minCost = 0, oilBank[0]
for i in range(N-1):
    if oilBank[i] < minCost:
        minCost = oilBank[i]
    sum += minCost * distance[i]
print(sum)