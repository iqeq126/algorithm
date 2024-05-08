from collections import deque
import sys
input, print = sys.stdin.readline, sys.stdout.write
for _ in range(int(input())):
    n, m = map(int, input().split())
    res = deque(map(int, input().split()))
    lst = deque(i for i in range(len(res)))
    answer = 0
    while True:
        if res[0] >= max(res):
            answer += 1
            if lst[0] == m: break
            else:
                res.popleft()
                lst.popleft()
        else:
            res.rotate(-1)
            lst.rotate(-1)
    print(f"{answer}\n")

