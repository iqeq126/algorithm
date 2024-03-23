import sys
input = sys.stdin.readline
iron_bar = input().rstrip("\n")
lazer = []
res = 0
for i in range(len(iron_bar)):
    if iron_bar[i] == '(':
        lazer.append('(')
    else:
        lazer.pop()
        if iron_bar[i-1] == '(':
            res += len(lazer)
        else:
            res += 1
print(res)