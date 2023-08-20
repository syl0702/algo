def solution(numbers):
    answer = set()
    for n in range(len(numbers)):
        for i in range(n+1, len(numbers)):
            answer.add(numbers[n] + numbers[i])
    answer = list(answer)
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))