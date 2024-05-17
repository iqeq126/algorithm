import sys
input, print = sys.stdin.readline, sys.stdout.write
t = int(input())
for _ in range(t):
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    lst = list(map(int, input().split()))
    for num in lst:
        print('1\n') if num in s else print('0\n')