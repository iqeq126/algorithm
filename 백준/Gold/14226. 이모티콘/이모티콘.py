from collections import deque
n = int(input())
def bfs(n):
    q = deque()
    q.append((1, 0, 0))
    res = 0
    visited = set()
    visited.add((1,0))
    while q:
        imti, size, time = q.popleft()
        if size == n:
            res = time-1
            break
        if (imti, imti) not in visited:
            visited.add((imti, imti))
            q.append((imti, imti, time+1))
        if (imti+size, size) not in visited:
            visited.add((imti+size, size))
            q.append((imti+size, size, time+1))
        if imti > 1 and (imti-1, size) not in visited:
            visited.add((imti-1, size) )
            q.append((imti-1, size, time+1))
    return res
print(bfs(n))