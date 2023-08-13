# 1 => 1
# 2 => 2
# 3 => 3
# 4 => 1
# 5 => 2
# 6 => 3
# 7 => 4
# 8 => 2
# 9 => 1
import math
import sys
N = int(sys.stdin.readline())
_list = [100000] * (2 * N + 1)
for i in range(1, N + 1):
    if i ** 2 <= N + 1:
        _list[i ** 2] = 1

for i in range(2, N+1):
    for j in range(1, int(math.sqrt(N) + 1)):
        if _list[ i ] > _list[(i - j*j)] + _list[j*j]:
            _list[ i ] = _list[(i - j*j)] + _list[j*j]
print(_list[N])
