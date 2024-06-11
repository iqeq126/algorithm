import sys
input = sys.stdin.readline
N = int(input())
buildings = list(map(int, input().split()))
cnt_lst = [0] * (N+1)
for i in range(N):
    max_lev = -sys.maxsize
    for j in range(i+1, N):
        lev = ( buildings[j] - buildings[i]) / (j - i)
        if lev > max_lev:
            cnt_lst[i] += 1
            cnt_lst[j] += 1
            max_lev = lev
print(max(cnt_lst))
