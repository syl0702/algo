import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    codes = input()
    temp = []
    for code in codes:
        if code == '{' or code == '(':
            temp.append(code)
        elif len(temp) and code == ')' and temp[-1] == '(':
            temp.pop()
        elif len(temp) and code == '}' and temp[-1] == '{':
            temp.pop()
        elif code == '}' or code == ')':
            temp.append(code)

    if len(temp) == 0:
        result = 1
    else:
        result = 0
