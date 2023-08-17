def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if sum(d) <= budget:
            answer = len(d)
        else:
            d.pop()
            continue
    return answer

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))