import sys
input = sys.stdin.readline
s = input().rstrip('\n')
b = list(input().rstrip('\n'))
lb = len(b)
stack = []
for _ in s:
    stack.append(_)
    if stack[-lb:] == b:
        for i in range(lb):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print(*stack, sep="")