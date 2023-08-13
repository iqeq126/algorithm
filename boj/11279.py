import sys
from queue import PriorityQueue
pq = PriorityQueue()
input = sys.stdin.readline
t, buf = int(input()), 0
for i in range(t):
    num = int(input())
    if num == 0:
        if pq.empty():
            print(0)
        else:
            print(-pq.get())
    else:
        pq.put(-num, num)