def solution(n, t):
    answer = 0
    answer = n * (2**t)
    return answer

print(solution(2, 10))
print(solution(7, 15))