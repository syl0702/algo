def solution(score):
    answer = []
    temp =[]
    for i in range(len(score)):
        temp.append(sum(score[i]) / 2)
        sorted_temp = sorted(temp, reverse = True)
        answer = [sorted_temp.index(s)+1 for s in temp]
    return answer

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))