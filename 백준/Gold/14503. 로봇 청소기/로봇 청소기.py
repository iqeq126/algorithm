from collections import deque
import sys
input = sys.stdin.readline
# 초기화
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
q = deque()
res = 0
room = [list(map(int, input().split())) for _ in range(N)]
q.append((r, c))
def bfs(res, d):
    while q:
        cy, cx = q.popleft()
        if room[cy][cx] == 0:
            room[cy][cx] = -1
            res += 1
        is_dirty = False
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if room[ny][nx] == 0:
                    is_dirty = True
        if not is_dirty:
            py, px = cy-dy[d], cx-dx[d]
            if 0 <= py < N and 0 <= px < M:
                if room[py][px] == 1:
                    break
                else:
                    q.append([py, px])
                    continue
        else:
            while True:
                d = (d-1) % 4
                ny, nx = cy+dy[d], cx+dx[d]
                if 0 <= ny < N and 0 <= nx < M:
                    if room[ny][nx] == 0:
                        q.append([ny, nx])
                        break

    return res
print(bfs(res, d))