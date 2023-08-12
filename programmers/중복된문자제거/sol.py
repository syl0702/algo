def solution(my_string):
    answer = ''
    check = []
    temp = list(my_string)
    # print(temp)
    for char in temp:
        if char not in check:
            check.append(char)
            # temp.pop(char)
            
        else:
            pass
    for c in check:
        answer += c

    return answer

print(solution("people"))
print(solution("We are the world"))