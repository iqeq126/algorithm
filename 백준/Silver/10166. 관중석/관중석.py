import math
def getBleachers():
    N, M = map(int, input().split())
    s = [[False] * 2001 for _ in range(2001)]
    res = 0
    for i in range(N, M+1):
        for j in range(1, i+1):
            k = math.gcd(i, j)
            if not s[i//k][j//k]:
                res += 1
                s[i//k][j//k] = True
    print(res)
getBleachers()