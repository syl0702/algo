def solution(s):
    answer = 0
    temp = []
    pairs = {'[': ']', '{': '}', '(': ')'}
    for i in range(len(s)):
        # 이어 붙이기
        s1 = s[i:] + s[:i]
        while True:
            length = len(s1)
            s1 = s1.replace("()", "")
            s1 = s1.replace("[]", "")
            s1 = s1.replace("{}", "")
            if len(s1) == 0:
                answer += 1
                break
            if length == len(s1): # 소거 작업 후에도 길이 변화가 없는 경우
                break
        # if temp and temp[-1] in pairs and s[0] == pairs[temp[-1]]:
        #     temp.pop()
        #     print(s1)
        #     answer+=1
        # else:
        #     temp.append(s[0])
        #     continue
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))