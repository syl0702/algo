def solution(s):
    s1 = list(s)
    s1 = ' '.join(s1).split()
    s2 = list(map(int, s1))
    print(s2)
    answer = ''
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))