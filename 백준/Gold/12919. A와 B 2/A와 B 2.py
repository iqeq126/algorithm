import sys
input = sys.stdin.readline
condition = True
S = list(input().strip('\n'))
T = list(input().strip('\n'))
global res
res = 0
def ST(s, t):
    global res
    if len(s) == len(t):
        if s == t:
            res = 1
        return
    if t[0] == 'B':
        t2 = t[1:]
        rt = t2[::-1]
        ST(s, rt)
    if t[-1] == 'A':
        ST(s, t[:len(t)-1])

ST(S, T)
print(res)