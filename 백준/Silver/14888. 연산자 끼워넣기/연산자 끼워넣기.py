import sys, operator
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
cmd = list(map(int, input().split()))
M, m = -sys.maxsize, sys.maxsize
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
def dfs(i, value):
    global M, m
    if i == n:
        M, m = max(M, value), min(m, value)
    else:
        idx = 0
        for _ in '+-*/':
            if cmd[idx] > 0:
                cmd[idx] -= 1
                dfs(i+1, int(ops[_](value, lst[i])))
                cmd[idx] += 1
            idx += 1
dfs(1, lst[0])
print(M, m, sep="\n")