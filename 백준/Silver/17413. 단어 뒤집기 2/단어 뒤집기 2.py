S = input() + ' '
stack = []
res = []
is_in_bracket = False
for s in S:
    if s == '<':
        is_in_bracket = True
        res.extend(stack[::-1])
        stack = []
    stack.append(s)

    if s == '>':
        is_in_bracket = False
        res.extend(stack[:])
        stack = []
    if s == ' ' and not is_in_bracket:
        stack.pop()
        res.extend(stack[::-1])
        stack = []
        res.extend(' ')
if res[0] == ' ': res.pop()
print(*res, sep="")