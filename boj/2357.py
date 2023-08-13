import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M = map(int, input().split())
_list = []
for i in range(N):
    num = int(input())
    _list.append(num)



for i in range(M):
    a, b = map(int, input().split())
    buf_list = [_list[i] for i in range(a, b)]
    print("{} {}\n".format(min(buf_list), max(buf_list)))