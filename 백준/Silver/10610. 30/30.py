N = sorted(list(map(str, input().strip())), reverse=True)
if sum(map(int, N)) % 3 != 0 or '0' not in N:
    print(-1)
else:
    for i in range(len(N)):
        for j in range(i+1, len(N)):
            if int(''.join(N)) % 30 == 0:
                print(int(''.join(N)))
                exit(0)
            N[i], N[j] = N[j], N[i]