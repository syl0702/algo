def solution(message):
    answer = 0
    for char in message:
        answer += len(message) * 2
        return answer

print(solution("happy birthday!"))
print(solution("I love you~"))