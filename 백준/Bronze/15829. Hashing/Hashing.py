N = int(input())
s = input().rstrip()
res = 0
for i in range(N):
    res = ( res + ( ord(s[i])-ord('a')+1 ) * (31 ** i) ) % 1234567891
print(res)