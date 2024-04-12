n = int(input())
fac = [i for i in range(n+1)]
for i in range(2, n+1):
    fac[i] = ( fac[i] * fac[i-1] )
    while fac[i] % 10 == 0:
        fac[i] //= 10
    fac[i] %= 1000000000000
print(f"{fac[n]%100000:0>5}")