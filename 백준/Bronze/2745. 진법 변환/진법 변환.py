from collections import defaultdict
dic = defaultdict(int)
for i in range(65, 91):
    dic[chr(i)] = i - 55
N, B = input().split()
res = 0
for i in range(len(N)):
    if N[i] in dic:
        res += dic[N[i]] * (int(B) ** (len(N)-1 - i))
    else:
        res += int(N[i]) * (int(B) ** (len(N)-1 - i))
print(res)