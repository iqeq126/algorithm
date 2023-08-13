import sys
from queue import PriorityQueue
pq = PriorityQueue()
input = sys.stdin.readline
t = int(input())
for i in range(t):
    num = int(input())
    if num == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[1])
    else:
        if num > 0:
            pq.put((num, num))
        else:
            pq.put((-num, num))