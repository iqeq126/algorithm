import sys
input, print = sys.stdin.readline, sys.stdout.write
pattern = input() # 패턴 입력
N = int(input()) # 숫자 입력 ( 파일 수 )
Files = [input() for _ in range(N)] # 파일명 입력
def checkPattern(file):
    # pattern Length, flie Length
    plen, flen = len(pattern), len(Files[file])
    DP = [[0 for _ in range(flen+1)] for i in range(plen+1)]
    DP[0][0] = 1
    for p in range(1, plen+1):
        cP = 0 # checkPattern
        for f in range(flen+1):
            if pattern[p-1] == '*':
                DP[p][f] = cP = (cP == 1 or DP[p-1][f] == 1)
            elif f:
                DP[p][f] = ( DP[p-1][f-1] and pattern[p-1] ) == Files[file][f-1]
    if DP[plen][flen]: return True
for f in range(N):
    if checkPattern(f): print(Files[f])
