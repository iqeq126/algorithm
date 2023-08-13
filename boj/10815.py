import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
N_list = set(map(int, input().split()))
M = int(input())
M_list = set(map(int, input().split()))
for i in M_list:
    if i in N_list:
        print("1 ")
    else:
        print("0 ")
print("\n")