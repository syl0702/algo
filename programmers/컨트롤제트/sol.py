def solution(s):
    answer = 0
    temp = []
    s1 = s.split()
    for n in s1:
        if n == 'Z':
            temp.pop()
            continue
        
        temp.append(int(n))
    answer = sum(temp)
    

    return answer

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))