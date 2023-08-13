s1 = input()
s2 = input()
s1 = "-" + s1
s2 = "-" + s2
y, x = len(s1)-1, len(s2)-1
LCS = [ [0 for i in range(1002)] for j in range(1002)]
LCS2 = []
for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0 or j == 0:
            LCS[0][0] = 0
        elif s1[i] == s2[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
while y >= 0 and x >= 0:
    if LCS[y-1][x] == LCS[y][x]:
        y -= 1
    elif LCS[y][x-1] == LCS[y][x]:
        x -= 1
    else:
        LCS2.append(s2[x])
        x -= 1
        y -= 1
LCS2 = LCS2[::-1]
print(max(max(LCS)))
print(*LCS2[:], sep="")