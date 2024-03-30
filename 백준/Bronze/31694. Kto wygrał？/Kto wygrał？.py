Algosia = list(map(int, input().split()))
Bajtek = list(map(int, input().split()))
if sum(Algosia) > sum(Bajtek):
    print("Algosia")
elif sum(Algosia) < sum(Bajtek):
    print("Bajtek")
else:
    i = 10
    tag = -1
    while i > 0:
        if Algosia.count(i) > Bajtek.count(i):
            tag = 0
            break
        elif Algosia.count(i) < Bajtek.count(i):
            tag = 1
            break
        i -= 1
    if tag == -1:
        print("remis")
    elif tag == 0:
        print("Algosia")
    else:
        print("Bajtek")
