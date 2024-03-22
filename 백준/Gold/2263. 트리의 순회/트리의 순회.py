import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pre_order = [0] * (n+1)
idx = 0
for i in in_order:
    pre_order[i] = idx
    idx += 1
def get_pre_order(in_odr_s, in_odr_e, po_odr_s, po_odr_e):
    if in_odr_s > in_odr_e or po_odr_s > po_odr_e:
        return

    root = post_order[po_odr_e]
    print(root, end = " ")

    left =pre_order[root] - in_odr_s
    right = in_odr_e - pre_order[root]

    get_pre_order(in_odr_s, in_odr_s + left - 1, po_odr_s, po_odr_s + left - 1)
    get_pre_order(in_odr_e - right + 1, in_odr_e, po_odr_e -right, po_odr_e - 1)
get_pre_order(0, n-1, 0, n-1)