N = int(input())
L = [[1 for i in range(10)] for j in range(N)]
L[0][0], mod = 0, 10 ** 9
for i in range(1,N):
    for j in range(10):
        if j == 0:
            L[i][j] = L[i-1][1]
        elif j == 9:
            L[i][j] = L[i-1][8]
        else:
            L[i][j] = (L[i-1][j-1] + L[i-1][j+1])
print(sum(L[N-1]) % mod)
#L = [9,17]
#[L.append((2*(L[i-1]-1))%(10**9)) for i in range(2,N+1)]
#print(L[N-1])