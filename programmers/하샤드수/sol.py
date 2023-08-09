def solution(x):
    answer = True
    temp = list(map(int, str(x)))
    if x % sum(temp) == 0:
        answer = True
    else:
        answer = False
    
    return answer

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))