def solution(n):
    answer = 0
    if int(n ** 0.5)**2 == n:
        answer = 1
    else:
        answer = 2
    return answer

print(solution(144))
print(solution(976))