def solution(chicken):
    answer = 0
    while chicken >= 10:
        a, b = divmod(chicken, 10)
        answer += a
        chicken = a + b
    return answer

print(solution(100))
print(solution(1081))