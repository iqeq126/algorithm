import sys
input, print = sys.stdin.readline, sys.stdout.write
n = int(input())
lst = list(map(int, input().split()))
sum_lst = [0] * (n+1)
sum_lst[1] = lst[0]
for i in range(2, n+1):
    sum_lst[i] = sum_lst[i-1] + lst[i-1]
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(f"{sum_lst[b] - sum_lst[a-1]}\n")