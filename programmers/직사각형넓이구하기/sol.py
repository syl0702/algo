def solution(dots):
    answer = 0
    temp = []
    temp2 = []
    for i in range(len(dots)-1):
        for j in range(2):
            temp.append(abs(dots[i][0] - dots[i+1][0]))
            temp2.append(abs(dots[i][1]-dots[i+1][1]))
            answer = max(temp) * max(temp2)  
    return answer

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))