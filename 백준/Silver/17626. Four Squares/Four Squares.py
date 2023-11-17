
import sys
from math import sqrt

n = int(sys.stdin.readline().strip())
answerList = [0 for i in range(50001)]

answerList[1] = 1
for i in range(2, n+1):
    answerList[i] = min(1 + answerList[i-1], 4)
    answerList[i] = min(answerList[i], min(answerList[i-j*j]+1 for j in range(1, int(sqrt(i)+1))))

print(answerList[n])
