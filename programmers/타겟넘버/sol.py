def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        queue = []
        for l in leaves:
            queue.append(l + num)
            queue.append(l - num)
        leaves = queue
    
    for leaf in leaves:
        if leaf == target:
            answer += 1
    
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))

