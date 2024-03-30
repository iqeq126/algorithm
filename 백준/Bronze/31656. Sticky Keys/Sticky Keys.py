s, tmp = input(), ""
for i in s:
    if tmp != i:
        print(i,end="")
        tmp = i
print()