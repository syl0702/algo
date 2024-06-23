import re
def solution(s):
    answer = 0
    temp = []
    if len(s) % 2 != 0:
        answer == 0
    else:
        for i in range(len(s)):
            if temp and temp[-1] == s[i]:
                temp.pop()
            else:
                temp.append(s[i])
        # print(temp)
        if len(temp) == 0:
            answer += 1

    return answer

print(solution('baabaa'))
print(solution('cdcd'))