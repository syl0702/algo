def solution(s):
    s1 = list(map(int, s.split()))
    # print(s1)
    temp = []
    temp.append(min(s1))
    temp.append(max(s1))
    # print(temp)
    answer = ' '.join(map(str, temp))
    # print(result)
    # answer = ''
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))