def solution(s):
    answer = True
    stack = []
    for b in s:
        if b == '(':
            stack.append(b)
        elif len(b) and b == ')' and stack[-1] == '(':
            stack.pop()
        elif b == ')':
            stack.append(b)

    if len(stack) == 0:
        
        return True
    
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))