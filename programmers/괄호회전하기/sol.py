def solution(s):
    answer = 0
    temp = []
    pairs = {'[': ']', '{': '}', '(': ')'}
    for i in range(len(s)):
        s1 = s[i:] + s[:i]
        if temp and temp[-1] in pairs and s[0] == pairs[temp[-1]]:
            temp.pop()
            print(s1)
            answer+=1
        else:
            temp.append(s[0])
            continue
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))