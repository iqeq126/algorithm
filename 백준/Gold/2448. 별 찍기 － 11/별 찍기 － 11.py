import sys
sys.setrecursionlimit(10**7)
print = sys.stdout.write
N = int(input())
star_list = ["  *  ", " * * ", "*****"]
print_list = [ [' '] *2*N for _ in range((N))]
def star(n, x, y):
    if n == 1:
        for i in range(3):
            for j in range(5):
                print_list[x+i][y+j] = star_list[i][j]
        return 0
    next = n // 2
    star(next, x, y + 3*next)
    star(next, x + 3*next, y)
    star(next, x + 3*next, y + 6* next)

star(N // 3, 0, 0)
for i in range(N):
    print(''.join(print_list[i]))
    print('\n')