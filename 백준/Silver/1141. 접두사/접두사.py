import sys
input = sys.stdin.readline
n = int(input())
words = sorted([input().rstrip('\n') for _ in range(n)], key = lambda x: len(x))
res = 0

for i in range(n):
    is_prefix = False
    for j in range(i+1, n):
        if words[i] == words[j][:len(words[i])]:
            is_prefix = True
            break
    if not is_prefix:
        res += 1

print(res)