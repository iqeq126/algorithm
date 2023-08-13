import sys
input = sys.stdin.readline
N = int(input())
_list = [0] * (N+1)
for i in range(2, N+1):
    _list[i] = _list[i-1] + 1
    if i % 2 == 0:
        _list[i] = min(_list[i], _list[i//2] + 1)
    if i % 3 == 0:
        _list[i] = min(_list[i], _list[i//3] + 1)
print(_list[N])
t = _list[N]
print(N, end = " ")
buf = N
