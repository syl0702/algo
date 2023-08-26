def solution(N, stages):
    answer = []
    temp = {}
    stages_len = len(stages)
    for i in range(1, N+1):
        if stages_len != 0:
            stage_count = stages.count(i)
            temp[i] = stage_count/stages_len
            stages_len -= stage_count
        else:
            temp[i] = 0
    
    answer = sorted(temp.keys(), key=lambda key: temp[key], reverse=True)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))