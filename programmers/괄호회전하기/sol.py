def solution(s):
    answer = -1
    temp = []
    pairs = {'[': ']', '{': '}', '(': ')'}
    for i in range(len(s)):
        s1 = s[i:] + s[:i]
        if temp[-1] in pairs and s[0] == pairs[temp[-1]]:
            temp.pop()
            print(s1)
        else:
            temp.append()
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))