import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
q = deque([N])
visited = [0 for _ in range(2000006)]
v_set = set()
def bfs():
    visited[N] = 0
    if N == K:
        print(0)
        return
    while q:
        v = q.popleft()
        _list = [2*v, v-1, v+1]
        for i in _list:
            if i == K:
                if i == 2*v: print(visited[v])
                else: print(visited[v]+1)
                return
            if visited[i] == 0 and 0<= i <= 100001:
                if i in v_set:
                    continue
                if i == 2*v:
                    visited[i] = visited[v]
                    v_set.add(i)
                else:
                    visited[i] = visited[v] + 1
                q.append(i)
    print(visited[K])
bfs()