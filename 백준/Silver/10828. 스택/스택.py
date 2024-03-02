import sys
input, print = sys.stdin.readline, sys.stdout.write
N = int(input())
stack = []
for i in range(N):
    commands = list(input().split())
    if len(commands) == 1:
        if commands[0] == "top":
            print(f"{stack[-1]}\n") if stack else print("-1\n")
        if commands[0] == "empty":
            print("0\n") if stack else print("1\n")
        if commands[0] == "size":
            print(f"{len(stack)}\n")
        if commands[0] == "pop":
            print(f"{stack.pop(-1)}\n") if stack else print("-1\n")
    if len(commands) == 2:
        if commands[0] == "push":
            stack.append(commands[1])