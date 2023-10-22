import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
res = sys.maxsize
N = int(input())
_list = list(map(int, input().split()))
s, e = 0, N-1
sVal, eVal = _list[s], _list[e]
while s != e:
    cur_res = abs(_list[s] + _list[e])
    if cur_res <= res:
        sVal, eVal = _list[s], _list[e]
        res = cur_res
    if abs(_list[s+1] + _list[e]) > abs(_list[s] + _list[e-1]):
        e -= 1
    else:
        s +=1
print(sVal, eVal)