import sys
input = sys.stdin.readline
n, m = map(int, input().split())
users = [ [sys.maxsize] * (n+1) for _ in range(n+1)]


def pass_through(i, k, j):
    return users[i][k] + users[k][j]


def floyd():
    for k in range(1, n+1):
        users[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j: continue
                if users[i][j] > pass_through(i, k, j):
                    users[i][j] = pass_through(i, k, j)

for i in range(m):
    a, b = map(int, input().split())
    users[a][b] = 1
    users[b][a] = 1

floyd()

res = sys.maxsize
min_users_num = sys.maxsize
for i in range(1, n+1):
    local_res = sum(users[i][1:])
    if res > local_res:
        res = local_res
        min_users_num = i

print(min_users_num)