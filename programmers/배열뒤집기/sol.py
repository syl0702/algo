# def solution(num_list):
#     answer = []

#     num_list.reverse()
#     answer = num_list

#     return answer

# def solution(num_list):
#     answer = []

#     for num in num_list:
#         answer.insert(0, num)
    
#     return answer

# print(solution([1, 2, 3, 4, 5]))

# def solution(num_list):
#     answer = num_list[::-1]
#     return answer

def solution(num_list):
    answer = []

    for i in range(len(num_list)):
        data = num_list[len(num_list)- i - 1]
        answer.append(data)

    return answer

print(solution([1, 2, 3, 4, 5]))