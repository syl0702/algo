def solution(array):
    answer = 0
    a = ''.join(map(str,array))
    answer = a.count('7')
    return answer

print(solution([7, 77, 17]))
print(solution([10, 29]))