global res
res = 0
N = int(input())
queen = [0 for _ in range(N)]
def check(C):
    for i in range(C):
        if (queen[C] == queen[i]) or (C-i == abs(queen[i] - queen[C])):
            return False
    return True
def nQueen(C):
    global res
    if C == N:
        res += 1
        return
    for i in range(N):
        queen[C] = i
        if check(C): nQueen(C+1)
nQueen(0)
print(res)