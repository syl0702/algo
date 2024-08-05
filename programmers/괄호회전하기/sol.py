def solution(s):
    answer = -1
    for i in range(len(s)):
        s1 = s[i:] + s[:i]
        
        print(s1)
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))