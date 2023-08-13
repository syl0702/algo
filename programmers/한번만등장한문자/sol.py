def solution(s):
    answer = ''
    s1 = sorted(s)
    for i in s1:
        if s1.count(i) == 1:
            answer += i
    return answer

print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))