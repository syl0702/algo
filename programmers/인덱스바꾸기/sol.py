def solution(my_string, num1, num2):
    answer = ''
    # print(type(my_string))
    # print(type(num1))
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    answer = "".join(my_string)
    return answer

print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))