from collections import deque
def bfs():
    n = int(input())
    q = deque()
    q.append((n, 0))
    visited = {}
    while True:
        x, res = q.popleft()
        if x == 1:
            return res
        res +=1
        if x % 3 == 0 and x//3 not in visited:
            visited[x//3] = res
            q.append((x//3, res))
        if x % 2 == 0 and x//2 not in visited:
            visited[x//2] = res
            q.append((x//2, res))
        if x-1 not in visited:
            visited[x-1] = res
            q.append((x-1, res))
print(bfs())