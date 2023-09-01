def solution(lines):
    answer = 0
    sets = []
    # for line in lines:
    #     line_set = [set(range(min(line), max(line)))]
    #     sets.append(line_set)
    # print(sets)

    

    
    sets = [set(range(min(line), max(line))) for line in lines]
    # print(sets)
    answer = len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    
    return answer

print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))