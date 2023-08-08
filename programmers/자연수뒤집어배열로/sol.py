def solution(n):
    answer = []
    temp = list(map(int, str(n)))
    temp.reverse()
    answer = temp
        
    return answer

print(solution(12345))