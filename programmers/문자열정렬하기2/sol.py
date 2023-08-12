def solution(my_string):
    answer = ''
    strin = my_string.lower()
    # print(strin)
    temp = list(strin)
    temp.sort()
    answer = "".join(temp)

    return answer

print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))