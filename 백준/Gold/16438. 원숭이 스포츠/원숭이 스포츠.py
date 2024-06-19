import sys
print = sys.stdout.write
n = int(input())
line_cnt = 0
res = [['' for _ in range(n+1)] for _ in range(8)]
MAX = 7
def divide_conquer(s, e, depth):
    global line_cnt
    if s >= e or depth == MAX:
        return
    line_cnt = max(line_cnt, depth)
    m = (s+e) // 2

    for i in range(s, e+1):
        res[depth][i] = 'A' if i <= m else 'B'

    depth += 1
    divide_conquer(s, m, depth)
    divide_conquer(m+1, e, depth)

divide_conquer(1, n, 0)

for i in range(line_cnt+1):
    for j in range(1, n+1):
        if res[i][j] == '':
            res[i][j] = 'A' if j % 2 else 'B'
        print(res[i][j])
    print('\n')

now_location = 0
while line_cnt != 6:
    for i in range(n):
        print('B') if i == now_location else print('A')
    print('\n')
    now_location = (now_location+1) % n
    line_cnt += 1