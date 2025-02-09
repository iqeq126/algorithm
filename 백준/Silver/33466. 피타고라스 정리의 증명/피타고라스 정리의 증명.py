import sys
input, print = sys.stdin.readline, sys.stdout.write
n = int(input())
for _ in range(n):
    t = int(input())
    i = t % 2
    t = t << 1
    print(f"{t-i}\n")
