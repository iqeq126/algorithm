import sys
input = sys.stdin.readline
N, M = map(int, input().split())
_list = [ list(map(int, input().split())) for _ in range(N)]
n_list = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        n_list[i][j] = _list[i][j]
for i in range(N):
    for j in range(N):
        if i < N-1:
            _list[i+1][j] += _list[i][j]
    for j in range(N):
        if j >= 1:
            _list[i][j] += _list[i][j-1]
for i in range(M):
    m_list = list(map(int, input().split()))
    if m_list[0] == m_list[2] and m_list[1] == m_list[3]:
        print(n_list[m_list[0]-1][m_list[1]-1])
    elif m_list[0] >=2 and m_list[1] >=2:
        print(_list[m_list[2]-1][m_list[3]-1]
                -_list[m_list[2]-1][m_list[1]-2]
                -_list[m_list[0]-2][m_list[3]-1]
                + _list[m_list[0]-2][m_list[1]-2]
        )
    elif m_list[0] >=2 and m_list[1] == 1:
        print(_list[m_list[2] - 1][m_list[3] - 1]
                - _list[m_list[0] - 2][m_list[3] - 1]
        )
    elif m_list[0] == 1 and m_list[1] >= 2:
        print(
            _list[m_list[2] - 1][m_list[3] - 1]
                - _list[m_list[2] - 1][m_list[1] - 2]
        )
    elif m_list[0] == 1 and m_list[1] == 1:
        print(_list[m_list[2] - 1][m_list[3] - 1])