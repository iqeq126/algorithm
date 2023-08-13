import sys
input = sys.stdin.readline
N = int(input())
s = [ list(map(int, input().strip('').rstrip('\n'))) for i in range(N) ]

def check(N,x, y, num):
    one, zero = True, True
    for i in range(x, x + N):
        for j in range(y, y+ N):
            if s[i][j] == 0:
                one = False
            if s[i][j] == 1:
                zero = False
            if one == False and zero == False:
                return -1
    if one:
        return 1
    elif zero:
        return 0

def q_tree(N, x, y, num):
    if N == 1:
        print(s[x][y], end="")
        return

    t = check(N,x,y,num)
    if t >= 0:
        print(t, end="")
    else:
        N = N // 2
        print("(", end="")
        for i in range(2):
            for j in range(2):
                q_tree(N,x+i*N, y+j*N, s[x+i*N][y+j*N])
        print(")", end="")
q_tree(N, 0, 0, s[0][0])
print()