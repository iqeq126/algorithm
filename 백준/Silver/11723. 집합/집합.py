import sys
input, print = sys.stdin.readline, sys.stdout.write
n = int(input())
s = set()
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == "add":
        if int(cmd[1]) not in s:
            s.add(int(cmd[1]))
    elif cmd[0] == "remove":
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
    elif cmd[0] == "check":
        print(f"1\n") if int(cmd[1]) in s else print(f"0\n")
    elif cmd[0] == "toggle":
        s.remove(int(cmd[1])) if int(cmd[1]) in s else s.add(int(cmd[1]))
    elif cmd[0] == "all":
        s = set(_+1 for _ in range(20))
    elif cmd[0] == "empty":
        s = set()