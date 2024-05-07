import sys
input, print = sys.stdin.readline, sys.stdout.write
T = int(input())
for t in range(T):
    n = int(input())
    lst = []
    for i in range(n):
        name, priority = input().split()
        lst.append([name, int(priority)])
    lst.sort(key=lambda x: x[1], reverse=True)
    for i in range(n-1):
        print(f"{lst[i][0]}, ")
    print(f"{lst[-1][0]}\n")