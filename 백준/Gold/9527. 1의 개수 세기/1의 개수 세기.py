import sys, math
sys.setrecursionlimit(10**7)
def one_count(num):
    if num <= 0: return 0
    exponent = int(math.log2(num))
    res = 2**exponent
    if res == num:
        return exponent * res // 2 + 1
    dif = num - res
    return one_count(res) + dif + one_count(dif)
a, b = map(int, input().split())
print(one_count(b) - one_count(a-1))