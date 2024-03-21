A, B = input(), input()
if A == B:
    print(0)
elif sorted(A) != sorted(B):
    print(-1)
else:
    res, j = 0, 1
    for i in range(1, len(A)+1):
        if A[-i] != B[-j]: res+=1
        else: j += 1
    print(res)