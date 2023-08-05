def solution(n):
    answer = []
    numbers = range(n+1)
    for num in numbers:
        if num % 2 != 0:
            answer.append(num)
    return answer

print(solution(10))
print(solution(15))