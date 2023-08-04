def solution(my_string, n):
    answer = ''
    result = []
    for strin in range(len(my_string)):
        result.append(my_string[strin] * n)
        answer = ''.join(result)
        
    return answer

print(solution("hello", 3))