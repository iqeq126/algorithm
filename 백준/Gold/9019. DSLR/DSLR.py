import sys
from collections import deque
input, print = sys.stdin.readline, sys.stdout.write
N = int(input())
def DSLR(x, ch):
    if ch == 'D': return (x * 2) % 10000
    if ch == 'S': return x-1 if x != 0 else 9999
    if ch == 'L': return (x % 1000) * 10 + x // 1000
    if ch == 'R': return (x % 10) * 1000 + x // 10

for i in range(N):
    ori, tar = map(int, input().split())
    q = deque()
    q.append((ori, ""))
    visited = [False] * 10001
    res = ""
    while q:
        ori, res = q.popleft()
        if ori == tar:
            print(res + '\n')
            break
        for ch in "DSLR":
            dslr = DSLR(ori, ch)
            if not visited[dslr]:
                visited[dslr] = True
                q.append((dslr, res + ch))