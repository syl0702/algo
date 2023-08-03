def solution(my_string):
    answer = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for strin in my_string:
        if strin not in vowels:
            answer += strin
    return answer

print(solution("bus"))
print(solution("nice to meet you"))