import sys
input = sys.stdin.readline
S = set()
N = int(input())
for _ in range(N):
    name, cmd = input().split()
    if cmd == "enter":
        S.add(name)
    if cmd == "leave" and name in S:
        S.remove(name)
print(*sorted(S, reverse=True), sep="\n")