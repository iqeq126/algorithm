import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
S = 0
for i in range(N):
    S +=  ( lst[i-2][0] * lst[i-1][1] - ( lst[i-1][0] * lst[i-2][1]) )* 0.5
print(f"{abs(S):.1f}")