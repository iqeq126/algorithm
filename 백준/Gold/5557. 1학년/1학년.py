import sys
input = sys.stdin.readline
N = int(input()) # 문자열 길이
lst = list(map(int, input().split())) # 초기 리스트
DP = [[0 for _ in range(N)] for _ in range(21)]  # DP 배열
DP[lst[0]][0] = 1 # 정답을 DP의 초기값에 저장
for i in range(1, N-1):
    for j in range(21): # 0 ~ 20의 범위를 지키기 위해
        if 0 <= j + lst[i] <= 20:
            DP[j + lst[i]][i] += DP[j][i -1]
        if 0 <= j - lst[i] <= 20:
            DP[j - lst[i]][i] += DP[j][i - 1]
print(DP[lst[N-1]][N-2])