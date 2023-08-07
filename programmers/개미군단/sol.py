def solution(hp):
    answer = 0
    if hp >= 5:
        answer += hp // 5
        if hp % 5 != 0:
            if hp % 5 >= 3:
                temp = hp % 5
                answer += temp // 3
                answer += temp % 3
            else:
                answer += hp % 5
    elif hp >= 3:
        answer += hp // 3
        answer += hp % 3
    else:
        answer += hp

    return answer

print(solution(23))
print(solution(24))
print(solution(999))