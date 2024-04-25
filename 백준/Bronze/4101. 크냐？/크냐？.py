import sys
input, print = sys.stdin.readline, sys.stdout.write
while True:
	n, m = map(int, input().split())
	if n == m == 0:
		break
	print("Yes\n") if n > m else print("No\n")