def solution(n):
    answer = 0
    if n == 1 or n ==2:
        answer+= 1
    elif n== 0:
        answer = 0

    else:
        answer += solution(n-1) + solution(n-2) % 1234567

    return answer

print(solution(3))
print(solution(5))