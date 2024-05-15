import sys
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
S = list(input().rstrip('\n'))
for i in range(m):
    cmd, s, e = map(int, input().split())
    if cmd == 1:
        buf = ""
        res = 0
        for j in range(s-1,e):
            if buf != S[j]:
                buf = S[j]
                res += 1
        print(res)
    if cmd == 2:
        for j in range(s-1, e):
            S[j] = chr( ord('A') + ( 1 + ord(S[j]) - ord('A')) % 26 )