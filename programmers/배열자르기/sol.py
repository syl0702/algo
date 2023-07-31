def solution(numbers, num1, num2):
    answer = []

    answer = numbers[num1 : num2 + 1]

    return answer

print(solution([1, 2, 3, 4, 5]))