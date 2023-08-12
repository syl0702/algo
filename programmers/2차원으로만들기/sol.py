def solution(num_list, n):
    answer = [[]]
    temp = []
    num = len(num_list) // n
    # for i in range(0, len(num_list), n):
    #     answer.append()
    for i in range(0, len(num_list), n):
        temp.append(num_list[i: i+n])
    
    answer = temp
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))