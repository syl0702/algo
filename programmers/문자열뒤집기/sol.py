def solution(my_string):
    answer = ''
    temp = list(my_string)
    temp.reverse()
    answer = ''.join(temp)
    return answer

print(solution("jaron"))
print(solution("bread"))