def solution(sides):
    answer = 0
    temp = []
    temp = sorted(sides)
    if temp[2] < temp[0] +temp[1]:
        answer += 1
    else:
        answer += 2
    return answer

print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))