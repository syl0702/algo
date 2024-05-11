def solution(s):
    answer = []
    s1= s.replace('0', '')
    s2 = bin(s1)
    print(s1)
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))