def solution(my_string):
    answer = []
    temp = []
    for char in my_string:
        if char.isdigit() == True:
            temp.append(char)
            answer = list(map(int, temp))
            answer.sort()
    return answer

print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))