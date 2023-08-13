import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
_list = list(map(int, input().split()))
ans = [[] for _ in range(N)]
def perfect_binary_tree(_list, level):
    if len(_list) == 1:
        ans[level].extend(_list)
        return
    length = len(_list)
    mid = length // 2
    ans[level].append(_list[mid])
    perfect_binary_tree(_list[:mid], level+1)
    perfect_binary_tree(_list[mid+1:], level+1)

perfect_binary_tree(_list, 0)

for i in range(N):
    if i == 0:
        print(ans[i][0])
    else:
        print(*ans[i])
