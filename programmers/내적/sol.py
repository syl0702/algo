def solution(a, b):
    answer = 0
    temp = 0
    temp = [x*y for x,y in zip(a, b)]
    answer = sum(temp)
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))