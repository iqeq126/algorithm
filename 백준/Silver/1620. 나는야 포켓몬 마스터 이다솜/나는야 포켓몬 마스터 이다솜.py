import sys
input, print = sys.stdin.readline, sys.stdout.write
N, M  = map(int, input().split())
encyclopedia = [""] + [input().rstrip() for _ in range(N)]
for _ in range(M):
    cmd = input().rstrip()
    try:
        print(f"{encyclopedia[int(cmd)]}\n")
    except:
        print(f"{encyclopedia.index(cmd)}\n")