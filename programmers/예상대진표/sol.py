def solution(n,a,b):
    answer = 0
    for i in range(n):
        if i % 2 == 0 and i == a:
            answer += 1
    

    return answer

print(solution(8, 4, 7))