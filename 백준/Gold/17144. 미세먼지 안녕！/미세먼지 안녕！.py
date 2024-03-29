import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())
room = [ list(map(int, input().split())) for _ in range(R)]
top, bottom = 0, 0
for i in range(R):
    if room[i][0] == -1:
        top, bottom = i, i + 1
        break

def diffuse_dust():
    drc = ((-1, 0), (1, 0), (0,-1), (0,1))
    diffused_dusts = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if room[r][c] <= 0: continue

            dust = room[r][c] // 5
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                    diffused_dusts[nr][nc] += dust
                    diffused_dusts[r][c] -= dust
    for r in range(R):
        for c in range(C):
            room[r][c] += diffused_dusts[r][c]

def clean_room(drc, air):
    r, c, d = air, 1 , 0
    prev = 0

    while True:
        nr, nc = r + drc[d][0], c + drc[d][1]

        if r == air and c == 0: break
        if not 0 <= nr < R or not 0 <= nc < C:
            d += 1
            continue
        room[r][c], prev = prev, room[r][c]
        r, c = nr, nc

for _ in range(T):
    diffuse_dust()
    clean_room(((0,1), (-1,0), (0,-1), (1,0)), top)
    clean_room(((0,1), (1,0), (0,-1), (-1,0)), bottom)

room[top][0], room[bottom][0] = 0, 0
print(sum(map(sum, room)))