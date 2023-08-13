import sys
N, K = map(int, sys.stdin.readline().split())
_list = list(map(int, sys.stdin.readline().split()))
s, e = -1,0
buf, answer =0, 10 ** 9
size = 0
while e < N:
    if buf < K:
        buf += _list[e]
        e+=1
    if buf >= K:
        while buf >= K:
            s += 1
            buf -= _list[s]
        size = e - s
        if size < answer:
            answer = size
if answer == 10 ** 9:
    print(0)
else:
    print(answer)