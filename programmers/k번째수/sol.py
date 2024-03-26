def solution(array, commands):
    answer = []
    for l in range(len(commands)):
        i = commands[l][0]
        j = commands[l][1]
        k = commands[l][2]
        temp = array[i-1:j]
        temp.sort()
        
        answer.append(temp[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))