def solution(my_string):
    my_strings = my_string.split()
    answer = int(my_strings[0])
    for i in range(1, len(my_strings),2):
        if my_strings[i] == '+':
            answer += int(my_strings[i+1])
        else:
            answer -= int(my_strings[i+1])
    
    return answer

print(solution("3 + 4"))

# eval()
# return eval(my_string)