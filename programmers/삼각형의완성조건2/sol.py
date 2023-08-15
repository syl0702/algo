def solution(sides):
    answer = 0
    sides.sort()
    # x가 가장 긴 변일 때
    for x in range(sides[1]+1, sides[0] + sides[1]):
        answer += 1
    
    # sides[1]이 가장 긴 변일 때
    for x in range(sides[1]-sides[0]+1, sides[1]+1):
        if x + sides[0] >= sides[1]:
            answer += 1
    return answer

print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))