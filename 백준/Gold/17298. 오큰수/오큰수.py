import sys
input, print = sys.stdin.readline, sys.stdout.write
n = int(input())
lst = list(map(int, input().split()))
o_lst = [-1] * n
stack = [0]
for i in range(1, n):
    while stack and lst[stack[-1]] < lst[i]:
        o_lst[stack.pop()] = lst[i]
    stack.append(i)
for nge in o_lst:
    print(f"{nge} ")