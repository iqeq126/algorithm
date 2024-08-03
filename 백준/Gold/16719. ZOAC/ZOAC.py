import sys
print = sys.stdout.write
s = input()
check = [False] * len(s)
index = [0] * len(s)
for i in range(len(s)):
    index[i] = ord(s[i])
def ZOAC(l, r):
    if l <= r:
        c = min(s[l:r+1])
        idx = s[l:r+1].index(c) + l
        check[idx] = True
        for i in range(len(s)):
            if check[i]:
                print(s[i])
        print("\n")
        ZOAC(idx+1, r)
        ZOAC(l, idx-1)

ZOAC(0, len(s)-1)