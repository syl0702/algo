def solution(answers):
    # answer = []
    # temp = []
    # one = [1, 2, 3, 4, 5]
    # two = [2, 1, 2, 3, 2, 4, 2, 5]
    # three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # num = 0
    # num2 = 0
    # num3 = 0
    # for i in range(len(answers)):
    #     one[i]
    #     if one[i] == answers[i]:
    #         num += 1   

    #     if two[i] == answers[i]:
    #         num2 += 1
        
    #     if three[i] == answers[i]:
    #         num3 += 1
    
    # temp = [num, num2, num3]
    # max_value = max(temp)

    # answer = [i + 1 for i, v in enumerate(temp) if v == max_value]

    # return answer
    
    answer = []
    temp = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num = 0
    num2 = 0
    num3 = 0

    # answers 리스트의 길이에 맞춰서 one, two, three 리스트의 항목을 반복해서 접근
    for i in range(len(answers)):
        if one[i % len(one)] == answers[i]:
            num += 1

        if two[i % len(two)] == answers[i]:
            num2 += 1
        
        if three[i % len(three)] == answers[i]:
            num3 += 1
    
    temp = [num, num2, num3]
    max_value = max(temp)

    answer = [i + 1 for i, v in enumerate(temp) if v == max_value]

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))