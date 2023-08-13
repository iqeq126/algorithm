t = int(input())
_list = [list(map(int, input().split())) for _ in range(t)]

paper = [0,0,0]
def check(t, x, y, n):
    for i in range(x, x+t):
        for j in range(y, y+t):
            if n != _list[i][j]:
                return False
    return True

def search(t, x, y, n):
    if check(t, x, y, n):
        paper[n] +=1
    else:
        t = t // 2
        for i in range(2):
            for j in range(2):
                search(t, x+i*t , y+j*t, _list[x+i*t][y+j*t])

search(t, 0, 0, _list[0][0])
print(paper[0])
print(paper[1])