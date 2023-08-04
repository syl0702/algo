def solution(my_string):
    answer = 0
    number = []

    for strin in my_string:
        try:
            number.append(int(strin))
            answer = sum(number)
        except:
            pass


    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))