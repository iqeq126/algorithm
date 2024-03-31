from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

seq_dxy = "RDUL"
dxy = [ [0, 1], [1, 0], [-1, 0], [0, -1]]
board = [] 
red_q, red_x, red_y = deque(), 0, 0
blue_q, blue_x, blue_y = deque(), 0, 0
for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'R':
            red_x, red_y = i, j
        elif board[i][j] == 'B':
            blue_x, blue_y = i, j

# 구슬을 움직이는 함수
def marble_move(x, y, dx, dy):
    move_count = 0
    nx, ny = x, y
    # 다음 칸이 벽면, 혹은 현재칸이 구멍인 경우 탈출
    while board[nx+dx][ny+dy] != '#' and board[nx][ny] != 'O':
        nx, ny = nx+dx, ny+dy
        move_count += 1

    return nx, ny, move_count

# 구슬을 탈출하는 함수
def marble_exit():
    # 빨간공, 파란공, 횟수에 대한 정보를 큐에 넣어준다
    red_q.append([red_x, red_y])
    blue_q.append([blue_x, blue_y])
    count_q = deque()
    count_q.append(1)
    sequence_q = deque([""])
    # 방문 정보를 set()에 저장시켜준다.
    visited = set()
    visited.add((red_x, red_y, blue_x, blue_y))
    # counter queue가 다 비워질 때까지
    while count_q:
        rx, ry = red_q.popleft()
        bx, by = blue_q.popleft()
        count = count_q.popleft()
        seq = sequence_q.popleft()
        # 만약 10 이상이 된다면 다음으로 넘어가준다.
        if count > 10:
            continue
        for i in range(4):
            seq_buf = seq + seq_dxy[i]
            # 구슬을 해당하는 범위까지 움직여준다.
            next_rx, next_ry, r_count = marble_move(rx, ry, dxy[i][0], dxy[i][1])
            next_bx, next_by, b_count = marble_move(bx, by, dxy[i][0], dxy[i][1])
            # 1. 만약 b구슬이 구멍에 나간 경우 문제 조건에 의해 무시해주고
            # 다음으로 넘어가준다.
            if board[next_bx][next_by] == 'O':
                continue

            # 2. 만약 r구슬만 구멍에 나간 경우 count를 반환해준다.
            if board[next_rx][next_ry] == 'O':
                return count, seq_buf

            # 3. 만약 빨간 구슬과 파란 구슬의 좌표가 같은 경우
            # 문제 조건에 의해 같은 칸에 존재할 수 없으므로
            if next_rx == next_bx and next_ry == next_by:
                # 둘 중에 count 값이 더 큰 것의 좌표를 한 칸 뒤로 미뤄준다.
                if r_count > b_count:
                    next_rx, next_ry = next_rx - dxy[i][0], next_ry - dxy[i][1]
                else:
                    next_bx, next_by = next_bx - dxy[i][0], next_by - dxy[i][1]

            # 만약 방문하지 않은 지점일 경우.
            # count값을 증가시키며 큐에 넣어준다.
            if (next_rx, next_ry, next_bx, next_by) not in visited:
                visited.add((next_rx, next_ry, next_bx, next_by))
                red_q.append([next_rx, next_ry])
                blue_q.append([next_bx, next_by])
                count_q.append(count+1)
                sequence_q.append(seq_buf)

    # queue를 빠져나왔다는 건 정답이 queue안에 없었다는 의미이므로
    # -1을 반환해준다.
    return [-1]

print(*marble_exit(), sep="\n")