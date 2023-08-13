import sys
t, buf = 0, 0
min, max = map(int, sys.stdin.readline().split())
_list = [2]
t_buf, t_buf2 = max, max
for i in range(min, max+1):
    for j in _list:
        if not i % (j ** 2):
            t_buf -= 1
        if i == j and i % j == 0:
            buf += 1
    if buf == 0 and i != 1:
        _list.append(i)
    if t_buf != t_buf2:
        t += 1
    buf = 0
    t_buf2 = t_buf
print(t)
print(_list)