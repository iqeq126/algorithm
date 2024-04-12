import sys
input, print = sys.stdin.readline, sys.stdout.write
t = int(input())
lst = [10] + [i for i in range(1, 10)]
for i in range(t):
    a, b = map(int, input().split())
    idx = 1
    for j in range(b):
        idx *= a
        idx %= 10
    print(f"{lst[idx]}\n")