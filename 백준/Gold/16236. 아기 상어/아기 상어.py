from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
shark_q, fish_q = deque(), deque()
N = int(input())
cea = list()
baby_shark, shark_size = 9, 2
for i in range(N):
    part_of_cea = list(map(int, input().split()))
    cea.append(part_of_cea)
    if baby_shark in cea[i]:
        shark_q.append((i, cea[i].index(baby_shark)))

y, x = shark_q[0]
def getDist(y, x, shark_size, shark_q):
    visited = [ [0] * N for _ in range(N)]
    distance = [ [0] * N for _ in range(N)]
    visited[y][x] = 1
    candidate_dist = []
    shark_q.append((y, x))
    while shark_q:
        cy, cx = shark_q.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                if cea[ny][nx] <= shark_size:
                    shark_q.append((ny, nx))
                    visited[ny][nx] = 1
                    distance[ny][nx] = distance[cy][cx] + 1
                    if cea[ny][nx] < shark_size and cea[ny][nx] > 0:
                        candidate_dist.append((ny, nx, distance[ny][nx]))
    return sorted(candidate_dist, key=lambda t: (-t[2], -t[0], -t[1]))

def getFish(y, x, shark_size, shark_q):
    count, res = 0, 0
    while True:
        fish_q = getDist(y, x, shark_size, shark_q)
        if len(fish_q) == 0:
            break
        ny, nx, fish = fish_q.pop()
        res += fish
        cea[y][x], cea[ny][nx] = 0, 0

        y, x = ny, nx
        count += 1
        if count == shark_size:
            shark_size += 1
            count = 0
    return res


print(getFish(y, x, shark_size, shark_q))
