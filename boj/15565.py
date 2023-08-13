import sys
N, K = map(int, sys.stdin.readline().split())
_list = list(map(int, sys.stdin.readline().split()))
s, e = -1,0
buf, answer =0, 1000000
size = 0
while e < N:
    if buf < K:
        if _list[e] == 1:
            buf += 1
        e += 1
    if buf == K:
        while buf == K:
            s += 1
            if _list[s] == 1:
                buf -= 1
        size = e - s
        if size < answer:
            answer = size

if answer == 1000000:
    print(-1)
else:
    print(answer)
# print(_list)