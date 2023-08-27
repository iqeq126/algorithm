import sys
input = sys.stdin.readline
N = int(input())
# 2차원 배열 입력
_list = [list(map(int, input().split())) for _ in range(N)]
# 경로 개수 배열
DP = [ [0 for _ in range(N)] for _ in range(N)]
# 초기값 설정
DP[0][0] = 1
t = 0
for i in range(N):
    for j in range(N):
				# 점프 정의 : 오른쪽이나 아랫쪽으로 이동
        I, J = i + _list[i][j], j + _list[i][j]
        if i == N-1 and j == N-1: # 둘 다 N-1이 되는 경우 탈출.
            break
        if I < N: # 오른쪽으로 이동하는 경우
            DP[I][j] += DP[i][j]

        if J < N: # 아랫쪽으로 이동하는 경우
            DP[i][J] += DP[i][j]

print(DP[N-1][N-1])