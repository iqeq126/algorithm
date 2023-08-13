import sys
N = int(sys.stdin.readline())
_list = list(map(int, sys.stdin.readline().split()))
_list = sorted(_list,key=abs)
print(_list)
s, e = 0, 1
S,E = s,e
answer = 10 ** 11
size = 10 ** 11
while s < e and e < N:
    buf = size
    size = abs(_list[s]+_list[e])
    if e < N-1 and buf >= size:
        e += 1
    else:
        s += 1
    if answer > size:
        answer = size
        S, E = s, e
print(_list[S], _list[E])