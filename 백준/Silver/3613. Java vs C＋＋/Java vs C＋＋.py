S = input().rstrip()
if S[0] == "_" or S[-1] == "_" or S[0].isupper() or "__" in S:
    print("Error!")
elif "_" in S and S != S.lower():
    print("Error!")
elif "_" in S:
    tag = False
    for i in range(len(S)):
        if S[i] == '_':
            tag = True
            continue
        elif tag:
            print(S[i].capitalize(), end="")
            tag = False
        else:
            print(S[i], end="")
    print()
else:
    for i in range(len(S)):
        if S[i].isupper():
            print(f"_{S[i].lower()}" , end="")
        else:
            print(S[i], end="")
    print()