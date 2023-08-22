def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        n = common[1] - common[0]
        answer = common[-1] + n
    elif common[1] // common[0] == common[2] // common[1]:
        k = common[1] // common[0]
        answer = common[-1] * k
    return answer

print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))