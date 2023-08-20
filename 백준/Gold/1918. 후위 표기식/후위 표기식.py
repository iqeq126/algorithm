import sys
input, print = sys.stdin.readline, sys.stdout.write
infix = list(input().rstrip(''))
operator = []
postfix = ''
for character in infix:
    if character.isalpha():
        postfix+=character
    else:
        if character == "(":
            operator.append(character)
        elif character == "*" or character == "/":
            while operator and (operator[-1] == "*" or operator[-1] == "/"):
                postfix += operator.pop()
            operator.append(character)
        elif character == "+" or character == "-":
            while operator and operator[-1] != "(":
                postfix += operator.pop()
            operator.append(character)
        elif character == ")":
            while operator and operator[-1] != "(":
                postfix += operator.pop()
            operator.pop()
while operator:
    postfix += operator.pop()
print(postfix)