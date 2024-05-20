from collections import defaultdict
import sys
input, print = sys.stdin.readline, sys.stdout.write
n, m = map(int, input().split())
dic = defaultdict(int)
for i in range(n):
    s = input().rstrip('\n')
    if len(s) >= m:
        dic[s] += 1
res = sorted(dic.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))
for s in res:
    print(f"{s[0]}\n")