import sys
input = sys.stdin.readline
# 입력 형식 지정
sudocu = [ list(map(int, input().strip('\n')) )for _ in range(9)]
rows = [[False for _ in range(9)] for _ in range(9)]
cols = [[False for _ in range(9)] for _ in range(9)]
subsudocu = [[False for _ in range(9)] for _ in range(9)]

# 좌표 전처리
for i in range(9):
    for j in range(9):
        if sudocu[i][j] != 0:
            rows[i][sudocu[i][j]-1] = True
            cols[j][sudocu[i][j]-1] = True
            subsudocu[3*(i//3) + j//3][sudocu[i][j]-1] = True
def solve(idx):
    if idx > 81:
        for i in range(9):
            print(*sudocu[i], sep="")
        sys.exit()
    x, y = (idx-1) // 9, (idx-1) % 9
    subNum = 3 * (x // 3) + y // 3
    if sudocu[x][y] == 0:
        for i in range(9):
            if(rows[x][i] == False) and (cols[y][i] == False) and (subsudocu[3*(x//3) + y//3][i] == False):
                sudocu[x][y] = i+1
                rows[x][i] = cols[y][i] = subsudocu[subNum][i] = True
                solve(idx+1)
                sudocu[x][y] = 0
                rows[x][i] = cols[y][i] = subsudocu[subNum][i] = False
    else:
        solve(idx + 1)
solve(1)