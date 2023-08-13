def solution(emergency):
    answer = []
    emergency_set = sorted(emergency)
    emergency_set.reverse()
    # print(emergency_set)
    for i in emergency:
        
        answer.append(emergency_set.index(i)+1)
    return answer

print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))