import sys
input = sys.stdin.readline
A, B = map(int, input().split())
i = 0
#_list = [[0 for i in range(6)] for j in range(6))
while A<B:
    i+=1
    #print(B)
    if B % 10 == 1:
        B = B // 10
    elif B % 2 == 0:
        B = B // 2
    else:
        break
if A==B:
    print(i+1)
else:
    print(-1)