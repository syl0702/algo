def solution(numbers):
    answer = []
    for n in range(len(numbers)):
        for i in range(n+1, len(numbers)):
            answer.append(numbers[n] + numbers[i])
    answer.sort()
    answer = list(set(answer))
    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))