def solution(order):
    answer = 0
    n = list(map(int, str(order)))
    
    if 3 in n:
        answer += 1
    if 6 in n:
        answer += 1
    if 9 in n:
        answer += 1
    

    # print(n) 
    return answer

print(solution(3))
print(solution(29423))