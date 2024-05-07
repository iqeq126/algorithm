import sys
input, print = sys.stdin.readline, sys.stdout.write
sets = set()
res = set()
while True:
    size = len(sets)
    s = input()
    if "000-00-0000" in s:
        break
    sets.add(s)
    if size == len(sets):
        res.add(s)
res = sorted(list(res))
for i in range(len(res)):
    print(f"{res[i]}")