import sys
T = int(sys.stdin.readline())
for _ in range(T):
    t = int(sys.stdin.readline())
    _list = [ list(map(int, sys.stdin.readline().split()) )for _ in range(2)]
    _answer = _list
    if t == 1:
        print(max(_list[0][0], _list[1][0]))
    elif t == 2:
        print(max(_list[0][0] + _list[1][1], _list[1][0] + _list[0][1]))
    else:
        _answer[0][0] = _list[0][0]
        _answer[0][1] = _list[0][1]+ _list[1][0]
        _answer[1][0] = _list[1][0]
        _answer[1][1] = _list[0][0] + _list[1][1]
        for i in range(2, t):
            # _answer[0][i]
            if _answer[1][i-1] > _answer[1][i-2]:
                _answer[0][i] += _answer[1][i-1]
            else:
                _answer[0][i] += _answer[1][i-2]
            # _answer[1][i]
            if _answer[0][i-1] > _answer[0][i-2]:
                _answer[1][i] += _answer[0][i-1]
            else:
                _answer[1][i] += _answer[0][i-2]
        print(max(_answer[0][t-1], _answer[1][t-1]))