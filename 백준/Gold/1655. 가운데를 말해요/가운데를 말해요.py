import sys
from heapq import *
input, print = sys.stdin.readline, sys.stdout.write
N = int(input())
maxHeap, minHeap = [], []
for _ in range(N):
    n = int(input())
    if len(maxHeap) == len(minHeap):
        heappush(maxHeap, -n)
    else:
        heappush(minHeap, n)
    if maxHeap and minHeap and -maxHeap[0] > minHeap[0]:
        maxValue, minValue = -heappop(maxHeap), heappop(minHeap)

        heappush(maxHeap, -minValue)
        heappush(minHeap, maxValue)
    print(f"{-maxHeap[0]}\n")