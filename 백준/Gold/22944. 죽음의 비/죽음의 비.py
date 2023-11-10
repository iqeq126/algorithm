import sys
from collections import deque
def solution():
    # 이동 범위 지정
    XY = [ [-1,0], [1,0],[0,-1], [0,1]]
    # 빠른 입력
    input = sys.stdin.readline
    # N : 가로세로 길이 H : 현재 체력 D: 내구도
    N, H, D = map(int, input().split())
    # 초기 배열 입력
    rainOfDeath = [list(input().strip('\n')) for _ in range(N)]
    # 방문 여부 배열
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 남은 우산 체력
    cost = 0
    # 이동 횟수
    cnt = 0
    # BFS 초기 위치 (S의 위치)
    player = deque()
    x, y = 0,0
    for i in range(N):
        for j in range(N):
            if rainOfDeath[i][j] == 'S':
                x, y = i,j
                break
    player.extend([(x, y, H, cost, cnt)])
    visited[x][y] = H  # 시작점 방문 처리
    while player:
        posX, posY, pHP, pUM, pCnt = player.pop()#, player.popleft(), player.popleft(), player.popleft(), player.popleft()
        #print(f"posX, posY, HP, pCost, pCnt : {posX}, {posY}, {pHP}, {pUM}, {pCnt}")
        # 상하좌우 탐색
        for dx, dy in XY:
            pX, pY = posX + dx, posY + dy
            pH,pU = pHP, pUM
            #print(DX, DY)
            if 0<= pX < N and 0<= pY < N:
                # E : 도착시
                if rainOfDeath[pX][pY] == 'E':
                    print(pCnt+1)
                    return

                # U : 우산일 경우 우산 바꿔주기
                if rainOfDeath[pX][pY] == 'U':
                    pU = D

                # 체력 깎아주기
                # 우산 내구도 >= 0
                if pU > 0: pU -= 1
                # 우산 내구도 == 0 and 체력 > 0
                else: pH -= 1

                # 체력 == 0 : 다시 탐색
                if pH == 0: continue

                # 현재 요소로 방문 처리
                if visited[pX][pY] < pH:# + pU:
                    visited[pX][pY] = pH# + pU
                    player.extendleft([(pX, pY, pH, pU, pCnt+1)])
    print(-1)
solution()