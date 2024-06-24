def solution(s):
    answer = False
    stack = []
    for i in range(len(s)):
        if stack and stack[-1]=='(' and s[i]==')':
            stack.pop()
        else:
            stack.append(s[i])
    # print(stack)
    if len(stack) == 0:
        answer = True
    
    return answer

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))