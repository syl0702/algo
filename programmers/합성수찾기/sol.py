def solution(n):
    answer = 0
    
    for num in range(n+1):
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1
        if count >= 3:
            answer += 1        
    return answer

print(solution(10))
print(solution(15))