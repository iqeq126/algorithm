import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
visited = [False for _ in range(2000006)]
res = 0
ans = sys.maxsize
def bfs(res=res, ans=ans):
    q = deque([[N, 0]])
    if N == K:
        print(0)
        print(1)
        return
    isFirst = True
    while q:
        v, cnt= q.popleft()
        _list = [ v-1, v+1, 2*v]
        visited[v] = True
        for i in _list:
            if i == K:
                if isFirst:
                    isFirst = False
                    ans = cnt+1
                    res+=1
                else:
                    if ans == cnt+1:
                        res += 1
                continue
            if not visited[i] and 0 <= i <= 100000:
                q.append([i, cnt+1])
    print(ans, res, sep="\n")
bfs()