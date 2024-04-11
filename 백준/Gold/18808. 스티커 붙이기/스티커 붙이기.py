import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for __ in range(n)]
# 스티커 회전
def rotate_sticker(s):
    nr, nc = len(s[0]), len(s)
    ns = [[0 for _ in range(nc)] for __ in range(nr)]
    q = deque()
    for i in range(nc):
        for j in range(nr):
            q.append(s[i][j])

    # 90도 회전
    for j in range(1, nc+1):
        for i in range(nr):
             ns[i][nc-j] = q.popleft()
    return ns

def is_attachable(r, c, s):
    sticker_r = 0
    for ri in range(r, r + len(s)):
        sticker_c = 0
        for ci in range(c, c + len(s[0])):
            if not (0 <= ri < n and 0 <= ci < m):
                return False

            if s[sticker_r][sticker_c] == 1 and board[ri][ci] == 1:
                return False

            sticker_c += 1
        sticker_r += 1
    return True

def find_sticker(s):
    for r in range(n):
        for c in range(m):
            res = is_attachable(r, c, s)
            if res:
                return r, c
    return -1, -1


for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    for _ in range(4):
        y, x = find_sticker(sticker)
        if x > -1 and y > -1:
            ri = 0
            for i in range(y, y + len(sticker)):
                ci = 0
                for j in range(x, x + len(sticker[0])):
                    if sticker[ri][ci] == 1:
                        board[i][j] = sticker[ri][ci]
                    ci += 1
                ri += 1
            break
        else:
            sticker = rotate_sticker(sticker)
print(sum(map(sum, board)))