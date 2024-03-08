import sys
input, print = sys.stdin.readline, sys.stdout.write
dxyz = [list(map(int, format(i, '03b'))) for i in range(8)]
def multi(a, b):
    matrix = [[0,0], [0,0]]
    for dx, dy, dz in dxyz:
        matrix[dx][dy] += (a[dx][dz]*b[dz][dy] % 1000)
    return matrix
def square(x, n):
    if n == 1: return x
    else:
        matrix = square(x, n//2)
        if n % 2: return multi(multi(matrix, matrix), x)
        else: return multi(matrix, matrix)
for _ in range(int(input())):
    matrix = [[6, -4], [1, 0]]
    res = square(matrix, int(input()))
    print(f"Case #{_+1}: {(res[0][0] + res[1][1] -1)%1000:0>3}\n")