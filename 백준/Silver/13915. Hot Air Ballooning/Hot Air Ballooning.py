import sys
input = lambda : sys.stdin.readline()
while True:
    try:
        n = int(input())
        res = set()
        for i in range(n):
            _s = ''
            t = input().rstrip('\n')
            for j in set(t):
                _s += j
            res.add(''.join(sorted(_s)))
        print(len(res))
    except:
        sys.exit()
