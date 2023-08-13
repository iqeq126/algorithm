import sys
answer = 0
t = int(sys.stdin.readline())
_list = [list(map(int, sys.stdin.readline().split())) for i in range(t)]
for i in range(t):
    for j in range(i+1, t):
        for k in range(j+1, t):
            a = (_list[i][0] - _list[j][0]) ** 2 + (_list[i][1] - _list[j][1]) ** 2
            b = (_list[i][0] - _list[k][0]) ** 2 + (_list[i][1] - _list[k][1]) ** 2
            c = (_list[j][0] - _list[k][0]) ** 2 + (_list[j][1] - _list[k][1]) ** 2
            if a + b == c or a + c == b or b + c == a:
                answer += 1
print(answer)