def solution(my_string, letter):
    answer = ''
    for strs in my_string:
        if strs not in letter:
            answer += strs

    return answer

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))


# def solution(my_string, letter)
#     answer = ''

#     for string in my_string:
#         if string != letter:
#             answer += string
#     return answer

# def solution(my_string, letter)
#   answer = ''
#   answer = my_string.replace(letter, '')

#   return answer