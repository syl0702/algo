def solution(n,a,b):
    answer = 0
    if abs(a-b) == 1:
        answer += 1
    

    return answer

print(solution(8, 4, 7))