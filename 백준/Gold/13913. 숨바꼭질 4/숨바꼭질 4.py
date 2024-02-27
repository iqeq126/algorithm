import sys, copy
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
q = deque([N])
visited = [0 for _ in range(2000002)]
root = [0 for _ in range(2000002)]
def bfs():
    visited[N] = 0
    if N == K:
        print(0)
        print(K)
        return
    while q:
        v = q.popleft()
        _list = [v-1, v+1, 2*v]
        for i in _list:
            if i == K:
                print(visited[v]+1)
                root[i] = v
                lst = [i]
                while root[i] != N:
                    lst.append(root[i])
                    i = root[i]
                lst.append(N)
                print(*lst[::-1])
                return
            if visited[i] == 0 and 0<= i <= 100001:
                visited[i] = visited[v] + 1
                root[i] = v
                q.append(i)
bfs()