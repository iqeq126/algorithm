import sys
from collections import defaultdict
input = sys.stdin.readline
dic = defaultdict(int)
N = int(input())
for _ in range(N):
    file_name, file_extension = input().split('.')
    dic[file_extension[:-1]] += 1
res = sorted(dic.items())
for i in range(len(res)):
    print(*res[i])