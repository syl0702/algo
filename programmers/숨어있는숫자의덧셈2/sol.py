import re
def solution(my_string):
    answer = 0
    temp = []
    numbers = my_string
    numbers = re.findall(r'\d+', numbers)
    # print(numbers)
    numbers = list(map(int, numbers))
    # print(numbers)
    answer = sum(numbers)
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))