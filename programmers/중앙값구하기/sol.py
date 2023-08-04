def solution(array):
    answer = 0
    array.sort()
    if len(array) % 2 != 0:
        answer = array[len(array)//2] 
    
    
    return answer

print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))