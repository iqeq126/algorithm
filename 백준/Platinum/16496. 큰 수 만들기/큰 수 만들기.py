from functools import cmp_to_key
import sys
input, print = sys.stdin.readline, sys.stdout.write
n = int(input())
def compare(l, r):
    if l == r: return -1
    lr, rl = l + r, r + l
    return 1 if lr > rl else -1

is_zero = True
s = list(input().split())
for i in range(len(s)):
    if s[i] != '0': is_zero = False
if is_zero: print("0\n")
else:
    s.sort(key=cmp_to_key(compare))
    for i in reversed(range(len(s))):
        print(f"{s[i]}")