from collections import deque

n, m, k = map(int, input().split())
dice_map = [ list(map(int, input().split())) for _ in range(n)]
dxy = [(1,0), (0, 1),(-1,0),(0,-1)]

dice = [1,2,3,4,5,6]
def get_dice(d, dir):
        R, D, L, U = 0, 1, 2, 3
        if dir == R:
                return [ d[3], d[1], d[0], d[5], d[4], d[2]]
        if dir == D:
                return [ d[1], d[5], d[2], d[3], d[0], d[4]]
        if dir == L:
                return [ d[2], d[1], d[5], d[0], d[4], d[3]]
        if dir == U:
                return [ d[4], d[0], d[2], d[3], d[5], d[1]]
dice_cx, dice_cy = 0, 0
X, Y = 0, 1
dir, res = 0, 0

while k:
        dice_nx, dice_ny = dice_cx + dxy[dir][X], dice_cy + dxy[dir][Y]

        if not ( ( 0 <= dice_ny < n ) and ( 0 <= dice_nx < m ) ):
                dir = (dir+2) % 4
                continue
        new_dice = get_dice(dice, dir)
        k -= 1
        q = deque()
        visited = [[False for _ in range(m)] for __ in range(n)]
        q.append((dice_ny, dice_nx))
        visited[dice_ny][dice_nx] = True
        cnt = 1
        while q:
                cy, cx = q.popleft()
                for dy, dx in dxy:
                        nx, ny = cx + dx, cy + dy
                        if not ( ( 0 <= ny < n ) and ( 0 <= nx < m ) ):
                                continue
                        if visited[ny][nx] or dice_map[ny][nx] != dice_map[dice_ny][dice_nx]:
                                continue
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        cnt += 1
        res += cnt * dice_map[dice_ny][dice_nx]

        if dice_map[dice_ny][dice_nx] < new_dice[-1]:
                dir = (dir+1) % 4
        elif dice_map[dice_ny][dice_nx] > new_dice[-1]:
                dir = (dir+3) % 4
        dice_cx, dice_cy = dice_nx, dice_ny
        dice = new_dice
print(res)