import sys
input = sys.stdin.readline
N= int(input())
score = [0] * (1001)
d = []
for i in range(N):
    D, W = map(int,input().split())
    d.append((W, D))
d.sort(reverse=True)
for i in range(N):
    for j in range(d[i][1], 0, -1):
        if score[j] == 0:
            score[j] = d[i][0]
            break
print(sum(score))
"""    
while d:
    if(t <=  max(d, key=lambda k: k[0])[1]):
        print(max(d, key=lambda k: k[0])[0], end=" {}".format(t))
        ans += max(d, key=lambda k: k[0])[0]
        d.pop(d.index(max(d, key=lambda k: k[0])))
    else:
        d.pop(d.index(min(d, key=lambda k: k[1])))
        t -= 1
    t += 1
    print()
print(ans)
"""