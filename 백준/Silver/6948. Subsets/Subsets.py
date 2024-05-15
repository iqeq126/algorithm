import sys
input = sys.stdin.readline
n = int(input())
s = [set() for _ in range(26)]
visited = [False for _ in range(26)]
cmd = sorted([list(input().split()) for i in range(n)], key=lambda x: x[2], reverse=True)

def solve(cmd):
    for i in range(n):
        megasets, _, subsets = cmd[i]
        mega, sub = ord(megasets)-ord('A'), ord(subsets)-ord('A')
        visited[mega] = True
        if ord(subsets) <= ord('Z'):
            s[mega] = set.union(s[mega], s[sub])
            visited[sub] = True
        else:
            s[mega].add(subsets)
solve(cmd)
cmd.sort()
solve(cmd)

for i in range(26):
    if visited[i]:
        print(f"{chr(ord('A')+i)} = ", end="")
        print('{', end="")
        print(*sorted(s[i]), sep=",", end="")
        print('}')