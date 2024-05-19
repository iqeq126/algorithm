from collections import defaultdict
dic = defaultdict(int)
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
	while lst[i] % 2 == 0:
		lst[i] //= 2

for i in range(n):
	dic[lst[i]] += 1

print(dic[max(dic, key=dic.get)])