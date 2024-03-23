charge = (500, 100, 50, 10, 5, 1)
res, i = 0, 0
money = 1000 - int(input())
for cg in charge:
    if money < cg:
        continue
    else:
        local_res = money // cg
        money -= cg * local_res
        res += local_res
print(res)