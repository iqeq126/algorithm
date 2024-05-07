from collections import deque

n, m = map(int, input().split())

def bfs():
    q = deque([(n, True, 0)]) 
    visited = [[False] * 2 for _ in range(m + 1)]
    visited[n][1] = True

    while q:
        num, chance, steps = q.popleft()

        if num == m:
            return steps

        next_moves = [num + 1, num * 2, num*10] if chance else [num + 1, num*2]
        for next_num in next_moves:
            if 0 < next_num <= m and not visited[next_num][chance]:
                visited[next_num][chance] = True
                q.append((next_num, chance and next_num != num * 10, steps + 1))

print(bfs())
